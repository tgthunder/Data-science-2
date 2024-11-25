import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class MatrixMultiplication {

    // Function to multiply two matrices
    public static int[][] multiplyMatrices(int[][] matA, int[][] matB) {
        int m = matA.length;
        int n = matA[0].length;
        int p = matB[0].length;

        int[][] result = new int[m][p];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < p; j++) {
                for (int k = 0; k < n; k++) {
                    result[i][j] += matA[i][k] * matB[k][j];
                }
            }
        }

        return result;
    }

    // Function to multiply two matrices using multithreading with one thread per row
    public static int[][] multiplyMatricesWithThreadPerRow(int[][] matA, int[][] matB) {
        int m = matA.length;
        int p = matB[0].length;
        int[][] result = new int[m][p];

        ExecutorService executor = Executors.newFixedThreadPool(m);

        for (int i = 0; i < m; i++) {
            int finalI = i;
            executor.execute(() -> {
                for (int j = 0; j < p; j++) {
                    for (int k = 0; k < matA[0].length; k++) {
                        result[finalI][j] += matA[finalI][k] * matB[k][j];
                    }
                }
            });
        }

        executor.shutdown();
        try {
            executor.awaitTermination(Long.MAX_VALUE, TimeUnit.NANOSECONDS);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        return result;
    }

    // Function to multiply two matrices using multithreading with one thread per cell
    public static int[][] multiplyMatricesWithThreadPerCell(int[][] matA, int[][] matB) {
        int m = matA.length;
        int p = matB[0].length;
        int[][] result = new int[m][p];

        ExecutorService executor = Executors.newFixedThreadPool(m * p);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < p; j++) {
                int finalI = i;
                int finalJ = j;
                executor.execute(() -> {
                    for (int k = 0; k < matA[0].length; k++) {
                        result[finalI][finalJ] += matA[finalI][k] * matB[k][finalJ];
                    }
                });
            }
        }

        executor.shutdown();
        try {
            executor.awaitTermination(Long.MAX_VALUE, TimeUnit.NANOSECONDS);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        return result;
    }

    // Main method for demonstration
    public static void main(String[] args) {
        int[][] matA = {{3, 6}, {12, 18}};
        int[][] matB = {{16, 28}, {45, 21}};

        int[][] resultSequential = multiplyMatrices(matA, matB);
        int[][] resultThreadPerRow = multiplyMatricesWithThreadPerRow(matA, matB);
        int[][] resultThreadPerCell = multiplyMatricesWithThreadPerCell(matA, matB);

        // Print results
        System.out.println("Sequential Result:");
        printMatrix(resultSequential);
        System.out.println("Result with Thread per Row:");
        printMatrix(resultThreadPerRow);
        System.out.println("Result with Thread per Cell:");
        printMatrix(resultThreadPerCell);
    }

    // Function to print a matrix
    public static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            for (int val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
    }
}
