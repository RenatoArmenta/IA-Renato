import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir variables lingüísticas
temperatura = ctrl.Antecedent(np.arange(0, 41, 1), 'temperatura')
humedad = ctrl.Antecedent(np.arange(0, 101, 1), 'humedad')
ventilador = ctrl.Consequent(np.arange(0, 101, 1), 'ventilador')

# Definir conjuntos difusos para temperatura
temperatura['frío'] = fuzz.trimf(temperatura.universe, [0, 0, 20])
temperatura['templado'] = fuzz.trapmf(temperatura.universe, [15, 20, 25, 30])
temperatura['caliente'] = fuzz.trimf(temperatura.universe, [25, 30, 40])

# Definir conjuntos difusos para humedad
humedad['baja'] = fuzz.trimf(humedad.universe, [0, 0, 40])
humedad['moderada'] = fuzz.trimf(humedad.universe, [30, 50, 70])
humedad['alta'] = fuzz.trimf(humedad.universe, [60, 100, 100])

# Definir conjuntos difusos para velocidad del ventilador
ventilador['baja'] = fuzz.trimf(ventilador.universe, [0, 0, 60])
ventilador['media'] = fuzz.trapmf(ventilador.universe, [40, 50, 70, 80])
ventilador['alta'] = fuzz.trimf(ventilador.universe, [60, 100, 100])

# Visualizar conjuntos difusos
temperatura.view()
humedad.view()
ventilador.view()

# Definir reglas difusas
regla1 = ctrl.Rule(temperatura['frío'] & humedad['baja'], ventilador['alta'])
regla2 = ctrl.Rule(temperatura['frío'] & humedad['moderada'], ventilador['media'])
regla3 = ctrl.Rule(temperatura['frío'] & humedad['alta'], ventilador['media'])
regla4 = ctrl.Rule(temperatura['templado'] & humedad['baja'], ventilador['media'])
regla5 = ctrl.Rule(temperatura['templado'] & humedad['moderada'], ventilador['media'])
regla6 = ctrl.Rule(temperatura['templado'] & humedad['alta'], ventilador['baja'])
regla7 = ctrl.Rule(temperatura['caliente'] & humedad['baja'], ventilador['baja'])
regla8 = ctrl.Rule(temperatura['caliente'] & humedad['moderada'], ventilador['baja'])
regla9 = ctrl.Rule(temperatura['caliente'] & humedad['alta'], ventilador['baja'])
regla10 = ctrl.Rule(temperatura['frío'] & humedad['baja'], ventilador['media'])
regla11 = ctrl.Rule(temperatura['templado'] & humedad['baja'], ventilador['alta'])
regla12 = ctrl.Rule(temperatura['frío'] & humedad['moderada'], ventilador['alta'])
regla13 = ctrl.Rule(temperatura['caliente'] & humedad['baja'], ventilador['alta'])

# Crear sistema de control difuso
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3, regla4, regla5, regla6, regla7, regla8, regla9, regla10, regla11, regla12, regla13])
sistema = ctrl.ControlSystemSimulation(sistema_control)

