

Credito #<-read.delim("clipboard")
str(Credito)

Credito$Credito <-factor(Credito$Credito)
Credito$Sexo <- factor(Credito$Sexo )
Credito$E.Civil <- factor(Credito$E.Civil)
Credito$Educacion <- factor(Credito$Educacion)
Credito$Prioridad <-factor(Credito$Prioridad)



# Transformación de la variable dependiente a binaria (0/1)


# Ajuste del modelo de regresión logística completo
modelglm1 <- glm(Credito ~ Sexo + E.Civil + Educacion + Prioridad + Edad + Tarjetas + Deuda + Saldo + CrediScore + Años_empleo + Ingresos, 
                 family = "binomial", data = Credito)

# Resumen del modelo completo
summary(modelglm1)

# Prueba de Chi-cuadrado para evaluar la significancia global del modelo
Chi2 <- modelglm1$null.deviance - modelglm1$deviance
q <- modelglm1$df.null - modelglm1$df.residual
p_value <- 1 - pchisq(Chi2, q)
cat("Prueba de Chi-cuadrado p-value:", p_value, "\n")


# Selección de variables con stepAIC
library(MASS)
modelglm2 <- stepAIC(modelglm1, direction = "backward")
summary(modelglm2)

# Ajuste de un modelo simplificado con variables seleccionadas
modelglm2 <- glm(Credito ~ E.Civil + Prioridad + Edad + Deuda + Saldo + CrediScore + Ingresos, 
                 family = "binomial", data = Credito)

# Mostrar resumen del modelo simplificado
summary(modelglm2)

# Prueba de Chi-cuadrado para el modelo simplificado
Chi2 <- modelglm2$null.deviance - modelglm2$deviance
q <- modelglm2$df.null - modelglm2$df.residual
p_value <- 1 - pchisq(Chi2, q)
cat("Prueba de Chi-cuadrado p-value para el modelo simplificado:", p_value, "\n")

# Interpretación de coeficientes y Odds Ratio para el modelo simplificado
odds_ratios2 <- exp(coef(modelglm2))
print(odds_ratios2)



"OBJETIVOS SECUNDARIOS PARA EL PROYECTO"
# Crear un nuevo dataframe con las características del cliente
nueva_persona <- data.frame(
  E.Civil = "Soltero",
  Prioridad = "No",
  Edad = 22,
  Deuda = 0,
  Saldo = 5000,
  CrediScore = 8,
  Ingresos = 1025
)


# Predecir la probabilidad usando el modelo ajustado modelglm2
predict(modelglm2, newdata = nueva_persona, type = "response")

# Mediante paquete Cálculo de Pseudo-R2
library(pscl)
pR2(modelglm2)


# ANÁLISIS EXPLORATORIO ---------------------------------------------------
# Diagrama de cajas (Cuantitativa y Cualitativa)
boxplot(Edad~Credito, data = Credito) 

# Porcentajes por columna (2 cualitativas)
prop.table(table(Credito$Credito,Credito$E.Civil), margin = 2)








