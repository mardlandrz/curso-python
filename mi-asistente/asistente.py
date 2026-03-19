import os

import anthropic


class Asistente:
    def __init__(self, nombre, api_key, model="claude-sonnet-4-0"):
        self.nombre = nombre
        self.model = model
        self.cliente = anthropic.Anthropic(api_key=api_key)
        self.historial = []

    def agregar_mensaje(self, rol, contenido):
        self.historial.append({
            "role": rol,
            "content": contenido,
        })

    def preguntar(self, pregunta):
        try:
            self.agregar_mensaje("user", pregunta)

            respuesta = self.cliente.messages.create(
                model=self.model,
                max_tokens=1024,
                system=f"Eres {self.nombre}, un asistente util y amigable que responde en espanol.",
                messages=self.historial,
            )

            texto = respuesta.content[0].text
            self.agregar_mensaje("assistant", texto)
            return texto

        except Exception as e:
            return f"Error real: {type(e).__name__} -> {e}"

    def ver_historial(self):
        if len(self.historial) == 0:
            print("No hay conversaciones aun")
            return

        for mensaje in self.historial:
            rol = mensaje["role"]
            contenido = mensaje["content"]

            if rol == "user":
                print(f"Tu:    {contenido}")
            else:
                print(f"{self.nombre}:   {contenido}")
            print("---")


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: no encontre la variable ANTHROPIC_API_KEY")
        print("Ejecuta: $env:ANTHROPIC_API_KEY='tu-clave'")
        return

    model = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-0")
    asistente = Asistente("Pythonito", api_key=api_key, model=model)

    print("=" * 40)
    print(f"Hola! Soy {asistente.nombre}")
    print("Escribe 'salir' para terminar")
    print("Escribe 'historial' para ver la conversacion")
    print("=" * 40)

    while True:
        pregunta = input("\nTu: ").strip()

        if pregunta == "":
            continue

        if pregunta.lower() == "salir":
            print("Hasta luego!")
            break

        if pregunta.lower() == "historial":
            asistente.ver_historial()
            continue

        print(f"\n{asistente.nombre}: ", end="")
        respuesta = asistente.preguntar(pregunta)
        print(respuesta)


if __name__ == "__main__":
    main()
