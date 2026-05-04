import java.util.Scanner;
import java.util.Locale;

public class AnaliseDesempenho {
    public static void main(String[] args) {
        // Configura o Scanner para aceitar ponto decimal (ex: 7.5) em vez de vírgula
        Scanner input = new Scanner(System.in).useLocale(Locale.US);

        System.out.print("Digite a quantidade de alunos na turma: ");
        int totalAlunos = Integer.parseInt(input.nextLine()); // Lê como texto e converte

        int aprovados = 0;
        int recuperacao = 0;
        int reprovados = 0;
        double somaNotas = 0;

        for (int i = 1; i <= totalAlunos; i++) {
            System.out.println("\n--- Aluno " + i + " ---");
            System.out.print("Nome: ");
            String nome = input.nextLine();

            System.out.print("Nota final (0 a 10): ");
            // Lê como texto e converte para double para evitar problemas no buffer
            double nota = Double.parseDouble(input.nextLine());

            // Validação da nota
            if (nota < 0 || nota > 10) {
                System.out.println("Nota inválida! Digite uma nota entre 0 e 10.");
                i--; // Volta um passo no loop para repetir este aluno
                continue;
            }

            somaNotas += nota;

            // Classificação da Situação (if / else)
            String situacao;
            if (nota >= 7) {
                situacao = "Aprovado";
                aprovados++;
            } else if (nota >= 5) {
                situacao = "Recuperação";
                recuperacao++;
            } else {
                situacao = "Reprovado";
                reprovados++;
            }

            // Classificação do Conceito (switch)
            char conceito;
            int notaInteira = (int) nota; 

            switch (notaInteira) {
                case 10:
                case 9:
                    conceito = 'A';
                    break;
                case 8:
                case 7:
                    conceito = 'B';
                    break;
                case 6:
                case 5:
                    conceito = 'C';
                    break;
                default:
                    conceito = 'D';
                    break;
            }

            System.out.println("Resultado: " + nome + " | Situação: " + situacao + " | Conceito: " + conceito);
        }

        // Relatório Final da Turma
        double mediaGeral = totalAlunos > 0 ? somaNotas / totalAlunos : 0;

        String situacaoTurma;
        if (mediaGeral >= 7) {
            situacaoTurma = "Turma com bom desempenho";
        } else if (mediaGeral >= 5) {
            situacaoTurma = "Turma em atenção pedagógica";
        } else {
            situacaoTurma = "Turma com desempenho crítico";
        }

        System.out.println("\n=================================");
        System.out.println("       RELATÓRIO DA TURMA       ");
        System.out.println("=================================");
        System.out.println("Total de alunos: " + totalAlunos);
        System.out.println("Quantidade de aprovados: " + aprovados);
        System.out.println("Quantidade em recuperação: " + recuperacao);
        System.out.println("Quantidade de reprovados: " + reprovados);
        System.out.printf("Média geral da turma: %.2f\n", mediaGeral);
        System.out.println("Situação geral: " + situacaoTurma);
        System.out.println("=================================");

        input.close();
    }
}