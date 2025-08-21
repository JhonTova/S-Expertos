import time
import os

class SistemaExpertoAutomotriz:
    def __init__(self):
        self.diagnosticos = {
            ("no_arranca", "luces_apagadas"): {
                "causa": "Batería descargada",
                "solucion": "Revisar y cargar la batería, verificar conexiones de los bornes"
            },
            ("no_arranca", "luces_encendidas"): {
                "causa": "Daño en el motor de arranque",
                "solucion": "Revisar motor de arranque, verificar conexiones eléctricas"
            },
            ("arranca", "se_apaga_acelerar"): {
                "causa": "Problema en el suministro de combustible",
                "solucion": "Revisar bomba de combustible, filtro y líneas de combustible"
            },
            ("arranca", "humo_escape"): {
                "causa": "Mezcla rica de combustible",
                "solucion": "Revisar sensores de oxígeno, inyectores y sistema de admisión"
            },
            ("arranca", "humo_blanco_constante"): {
                "causa": "Falla en la junta de culata",
                "solucion": "Revisar junta de culata, verificar niveles de refrigerante"
            },
            ("arranca", "humo_azul"): {
                "causa": "Quema de aceite en la cámara de combustión",
                "solucion": "Revisar anillos del pistón, válvulas y sellos de válvulas"
            },
            ("arranca", "humo_negro"): {
                "causa": "Mezcla muy rica de combustible",
                "solucion": "Limpiar o cambiar filtro de aire, revisar inyectores"
            },
            ("arranca", "ruido_motor"): {
                "causa": "Desgaste interno del motor",
                "solucion": "Revisar nivel de aceite, cojinetes y componentes internos"
            },
            ("arranca", "vibra_mucho"): {
                "causa": "Falla en soportes del motor o desbalance",
                "solucion": "Revisar soportes del motor y balanceado del cigüeñal"
            },
            ("arranca", "temperatura_alta"): {
                "causa": "Sobrecalentamiento del motor",
                "solucion": "Revisar radiador, termostato, bomba de agua y refrigerante"
            },
            ("arranca", "consume_mucho_combustible"): {
                "causa": "Mal funcionamiento del sistema de inyección",
                "solucion": "Revisar inyectores, sensores y sistema de encendido"
            },
            ("no_arranca", "hace_ruido_arranque"): {
                "causa": "Motor de arranque defectuoso",
                "solucion": "Cambiar motor de arranque o revisar conexiones"
            },
            ("arranca", "marcha_irregular"): {
                "causa": "Falla en el sistema de encendido",
                "solucion": "Revisar bujías, cables de bujía y bobinas de encendido"
            }
        }

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def hacer_pregunta(self, pregunta, opciones):
        while True:
            print(f"\n❓ {pregunta}")
            for i, opcion in enumerate(opciones, 1):
                print(f"   {i}. {opcion}")
            try:
                respuesta = input("\n👉 Selecciona una opción (número): ").strip()
                indice = int(respuesta) - 1
                if 0 <= indice < len(opciones):
                    return opciones[indice].lower().replace(" ", "_")
                else:
                    print(f"❌ Por favor, ingresa un número entre 1 y {len(opciones)}")
            except ValueError:
                print("❌ Por favor, ingresa un número válido")
            time.sleep(1)

    def preguntar_si_no(self, pregunta):
        while True:
            print(f"\n❓ {pregunta}")
            print("   1. Sí")
            print("   2. No")
            respuesta = input("\n👉 Selecciona una opción: ").strip().lower()
            if respuesta in ['1', 'si', 'sí', 's']:
                return True
            elif respuesta in ['2', 'no', 'n']:
                return False
            else:
                print("❌ Por favor, responde con 1 (Sí) o 2 (No)")
                time.sleep(1)

    def diagnosticar_vehiculo(self):
        print("\n🔍 Iniciando diagnóstico...")
        time.sleep(1)
        estado_arranque = self.hacer_pregunta(
            "¿Cuál es el estado de arranque de tu vehículo?",
            ["Arranca", "No arranca"]
        )
        if estado_arranque == "no_arranca":
            sintoma_secundario = self.diagnosticar_no_arranca()
        else:
            sintoma_secundario = self.diagnosticar_arranca()
        clave_diagnostico = (estado_arranque, sintoma_secundario)
        if clave_diagnostico in self.diagnosticos:
            self.mostrar_diagnostico(clave_diagnostico)
        else:
            candidatos = [k for k in self.diagnosticos.keys() if k[0] == estado_arranque]
            if candidatos:
                self.mostrar_diagnostico(candidatos[0])
            else:
                self.diagnostico_generico()

    def diagnosticar_no_arranca(self):
        luces_funcionan = self.preguntar_si_no("¿Las luces del tablero se encienden cuando giras la llave?")
        if not luces_funcionan:
            return "luces_apagadas"
        else:
            hace_ruido = self.preguntar_si_no("¿El motor hace algún ruido cuando intentas arrancarlo?")
            if hace_ruido:
                return "hace_ruido_arranque"
            else:
                return "luces_encendidas"

    def diagnosticar_arranca(self):
        problemas = [
            "Se apaga al acelerar",
            "Humo en el escape",
            "Humo blanco constante",
            "Humo azul",
            "Humo negro",
            "Hace ruidos extraños",
            "Vibra mucho",
            "Se sobrecalienta",
            "Consume mucho combustible",
            "Marcha irregular"
        ]
        tiene_problema = self.preguntar_si_no("¿Tu vehículo presenta algún problema mientras funciona?")
        if tiene_problema:
            problema = self.hacer_pregunta("¿Cuál de estos problemas presenta tu vehículo?", problemas)
            mapeo_problemas = {
                "se_apaga_al_acelerar": "se_apaga_acelerar",
                "humo_en_el_escape": "humo_escape",
                "humo_blanco_constante": "humo_blanco_constante",
                "humo_azul": "humo_azul",
                "humo_negro": "humo_negro",
                "hace_ruidos_extraños": "ruido_motor",
                "vibra_mucho": "vibra_mucho",
                "se_sobrecalienta": "temperatura_alta",
                "consume_mucho_combustible": "consume_mucho_combustible",
                "marcha_irregular": "marcha_irregular"
            }
            return mapeo_problemas.get(problema, problema)
        else:
            return "funciona_normal"

    def mostrar_diagnostico(self, clave):
        diagnostico = self.diagnosticos[clave]
        print("🎯 DIAGNÓSTICO ENCONTRADO")
        print(f"🔧 Causa probable: {diagnostico['causa']}")
        print(f"💡 Solución recomendada: {diagnostico['solucion']}")

    def diagnostico_generico(self):
        print("❓ DIAGNÓSTICO NO ESPECÍFICO")
        print("No se pudo determinar un diagnóstico específico")
        print("con los síntomas proporcionados.")
        print("\n💡 Recomendaciones generales:")
        print("• Revisar niveles de fluidos (aceite, refrigerante, etc.)")
        print("• Verificar el estado de la batería")
        print("• Consultar con un mecánico profesional")

    def ejecutar(self):
        while True:
            self.limpiar_pantalla()
            opcion = self.hacer_pregunta(
                "¿Qué deseas hacer?",
                ["Diagnosticar vehículo", "Salir"]
            )
            if opcion == "diagnosticar_vehículo":
                try:
                    self.diagnosticar_vehiculo()
                    input("\n🔄 Presiona Enter para continuar...")
                except KeyboardInterrupt:
                    print("\n\n❌ Diagnóstico cancelado por el usuario")
                    time.sleep(2)
            elif opcion == "salir":
                print("\n👋 ¡Gracias por usar el Sistema Experto Automotriz!")
                print("🚗 ¡Que tengas un buen viaje!")
                break

def main():
    print("🚀 Cargando Sistema Experto Automotriz...")
    time.sleep(2)
    sistema = SistemaExpertoAutomotriz()
    try:
        sistema.ejecutar()
    except KeyboardInterrupt:
        print("\n\n👋 Sistema cerrado por el usuario. ¡Hasta luego!")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        print("Por favor, reinicia el sistema.")

if __name__ == "__main__":
    main()
