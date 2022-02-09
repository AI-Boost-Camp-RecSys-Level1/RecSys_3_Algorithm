package RecSys_3_Algorithm.ijkimmy;

// 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 
// 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
// 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 
// 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

// Q
// length of numbers    1~7 (inclusive)
// val of numbers       0~9
// duplicates?          yes

// Solution
// max = sort input in reverse order
// store all prime numbers from 1..max
// permute for possible numbers

import java.util.Arrays;
import java.util.HashSet;

// 37m
public class programmers_gen_prime_num {
    public int solution(String numbers) {
        char[] cnums = numbers.toCharArray();
        Arrays.sort(cnums);
        
        int maxnum = 0;
        for(int i=cnums.length-1; i>=0; --i){
            maxnum *= 10;
            maxnum += cnums[i];
        }

        boolean[] isprime = new boolean[maxnum+1];
        Arrays.fill(isprime, true);
        isprime[0] = isprime[1] = false;
        for(int i=2; i<isprime.length; ++i){
            if(!isprime[i])
                continue;
            for(int j=i+i; j<isprime.length; j+=i)
                isprime[j] = false;
        }

        HashSet<Integer> primes = new HashSet<>();
        permute(numbers, new boolean[numbers.length()], isprime, "", primes);
        return primes.size();
    }

    public void permute(String numbers, boolean[] taken, boolean[] isprime, String permuted, HashSet<Integer> primes){
        if(!permuted.isEmpty() && isprime[Integer.valueOf(permuted)]){
            primes.add(Integer.valueOf(permuted));
        }

        for(int i=0; i<numbers.length(); ++i){
            if(!taken[i]){
                taken[i] = true;
                String next = permuted + numbers.charAt(i);
                permute(numbers, taken, isprime, next, primes);
                taken[i] = false;
            }
        }
    }
}
