import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Scanner sc = new Scanner(System.in);
        int input2 = 16;
        // int[] input1;
        // for (int i = 0; i < input2; i++) {
        //     input1[i] = sc.nextInt();
        // }
        int [] input1= {5, 123, 12, 45, 62, 77, 89, 23, 12, 14, 11, 14, 12, 90, 89, 12};
        System.out.println(findPassword(input1, input2));
    }

    public static int findPassword(int[] input1, int input2) {
        int max = input1[0];
        String s1, s2, s = "";
        for (int i = 1; i < input2; i++) {
            if (input1[i] > max) {
                max = input1[i];
            }
        }

        
        int freq[] = new int[max];
        for (int i : input1) {
            freq[i - 1]++;
        }
        int high_occ = 0, sec_high_occ = 0;
        for (int i = 0; i < max; i++) {
            if (freq[i] > 0 && freq[i] > freq[high_occ]) {
                if (freq[i] != freq[high_occ]) {
                    sec_high_occ = high_occ;
                }
                high_occ = i;
            } else if (freq[i] > 0 && freq[i] > freq[sec_high_occ]) {
                sec_high_occ = i;
            }
        }
        sec_high_occ = sec_high_occ + 1;
        high_occ = high_occ + 1;
        s1 = Integer.toString(sec_high_occ);
        s2 = Integer.toString(high_occ);
        s = s1 + s2;
        int c = Integer.parseInt(s);

        return c;
    }
}