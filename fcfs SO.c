#include <stdio.h>
#include <stdlib.h>

struct Proceso {
    char letra;
    int prioridad;
    int t_llegada;
    int t_cpu;
    int t_espera;
    int t_retorno;
};
// funcion principal
void fcfs(struct Proceso p[], int n);

int main() {
    struct Proceso procesos[5];
    // forma de abrir un archivo en C
    FILE *archivo = fopen("input.txt", "r");

    if (archivo == NULL) {
        printf("Error! No se pudo abrir el archivo\n");
        exit(-1);
    }

    for (int i = 0; i < 5; i++) {
        fscanf(archivo, " %c %d %d %d", &procesos[i].letra,
               &procesos[i].prioridad, &procesos[i].t_llegada, &procesos[i].t_cpu);
    }

    fclose(archivo);

    fcfs(procesos, 5);

    return 0;
}

void fcfs(struct Proceso p[], int n) {
    // Ordenar por tiempo de llegada y prioridad burbuja
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (p[j].t_llegada > p[j + 1].t_llegada ||
               (p[j].t_llegada == p[j + 1].t_llegada && p[j].prioridad > p[j + 1].prioridad)) {
                struct Proceso temp = p[j];
                p[j] = p[j + 1];
                p[j + 1] = temp;
            }
        }
    }


    int tiempoCPU = 0;
    // Nucleo de FCFS
    for (int i = 0; i < n; i++) {
        p[i].t_retorno = tiempoCPU + p[i].t_cpu - p[i].t_llegada;
        p[i].t_retorno = (p[i].t_retorno < 0) ? 0 : p[i].t_retorno; // en caso que el T-retorno sea mayor al tiempoCPU ACUMULADO
        p[i].t_espera =  p[i].t_retorno - p[i].t_cpu;

        tiempoCPU += p[i].t_cpu;
    }

    int tot_esp = 0;
    int tot_ret = 0;

    for (int j = 0; j < n; j++) {
        tot_esp += p[j].t_espera;
        tot_ret += p[j].t_retorno;
    }
    //calculo de los promedios
    double p_esp = (double)tot_esp / n;
    double t_retorno_promedio = (double)(tot_esp + tiempoCPU) / n;

    // Imprimir resultados
    printf("%s %7s %10s %10s %10s %10s\n", "Proceso", "Prio", "T-llegada", "T-CPU", "T-espera", "T-retorno");

    for (int i = 0; i < n; i++) {
        printf("%c %10d %10d %10d %10d %10d\n", p[i].letra,
               p[i].prioridad, p[i].t_llegada, p[i].t_cpu, p[i].t_espera, p[i].t_retorno);
    }

    printf("\nEl tiempo de retorno promedio es %.2lf\n", t_retorno_promedio);
    printf("El tiempo de espera promedio es %.2lf\n", p_esp);
}







