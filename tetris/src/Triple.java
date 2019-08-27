public class Triple {
    private int[] contents;

    public Triple() {
        contents = new int[3];
    }

    public Triple(int a, int b, int c) {
        contents = new int[3];

        contents[0] = a;
        contents[1] = b;
        contents[2] = c;
    }

    public int get(int i) {
        return contents[i];
    }
}
