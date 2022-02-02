class Solution {
    public int oddEvenJumps(int[] A) {
        int N = A.length;
        boolean[] starting = new boolean[N];
        boolean[] evenStarting = new boolean[N];
        starting[N-1] = true;
        evenStarting[N-1] = true;
        int count = 1;
        for (int start = N - 2; start >=0 ; start--) {
            int o = oddJump(start, A);
            int e = evenJump(start, A);
            if (o != -1 && evenStarting[o]) {
                starting[start] = true;
                count++;
            }
            evenStarting[start] = (e != -1 && starting[e]);
        }
        return count;
    }
    
    public int oddJump(int i, int[] A) {
        int v = A[i];
        int max = 100001;
        int jmax = -1;
        for (int j = i + 1; j < A.length; j++) {
            if (A[j] >= v && A[j] < max) {
                max = A[j];
                jmax = j;
            }
        }
        return jmax;
    }
public int evenJump(int i, int[] A) {
        int v = A[i];
        int min = -1;
        int jmin = -1;
        for (int j = i + 1; j < A.length; j++) {
            if (A[j] <= v && A[j] > min) {
                min = A[j];
                jmin = j;
            }
        }
        return jmin;
    }
}
                
