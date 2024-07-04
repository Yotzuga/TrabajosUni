# Cargar los datos

Credito  #<-read.delim("clipboard")


# Modelo inicial
modelo1 <- lm(Monto ~ Sexo + E.Civil + Educacion + Prioridad + 
                Edad + Tarjetas + Deuda + Saldo + CrediScore + 
                Años_empleo + Ingresos, data = Credito)

#resumen del modelo inicial
summary(modelo1)

modelo1


# Selección de variables con stepAIC
library(MASS)
stepAIC(modelo1, direction = "backward")

# Modelo final
modelo2 <- lm(Monto ~ E.Civil + Prioridad + Edad + Deuda + Saldo + CrediScore + Ingresos, data = Credito)


summary(modelo2)

# Prueba de normalidad de los errores
residuales <- modelo2$residuals

# QQ-Plot
library(car)
qqnorm(residuales)
qqline(residuales)


# Gráfico Q-Q Plot con intervalos de confianza
qqPlot(residuales)

# Prueba de Anderson-Darling
library(nortest)
ad.test(residuales)

# Evaluación de multicolinealidad
library(car)

vif(modelo2)


"OBJETIVOS SECUNDARIOS PARA EL PROYECTO"
# Crear un nuevo dataframe con las características del cliente
nuevo_cliente <- data.frame(
  E.Civil = "Soltero",
  Prioridad = "No",    # Asumimos que no es un cliente prioritario
  Edad = 22,           # Edad del cliente
  Deuda = 0,        # Monto de la deuda del cliente
  Saldo = 5000,        # Saldo del cliente
  CrediScore = 8,    # Puntaje de crédito del cliente
  Ingresos = 1025     # Ingresos del cliente
)

# Realizar la predicción utilizando el modelo ajustado
predict(modelo2, newdata = nuevo_cliente)

#(intervalo para un valor individual)
predict(modelo2, newdata = nuevo_cliente, interval = "predict", level = 0.95)















