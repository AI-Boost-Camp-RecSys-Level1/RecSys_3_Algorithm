package RecSys_3_Algorithm.ijkimmy.Pro;

// https://programmers.co.kr/learn/courses/30/lessons/43238
// n명이 입국심사를 위해 줄을 서서 기다리고 있습니다. 
// 각 입국심사대에 있는 심사관마다 심사하는데 걸리는 시간은 다릅니다. => int[] times
// 처음에 모든 심사대는 비어있습니다. 한 심사대에서는 동시에 한 명만 심사를 할 수 있습니다. 
// 가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사를 받을 수 있습니다. 하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있습니다.
// 모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.
// 입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때, 
// 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성해주세요.

// Q
// range of n               1~10^9 (inclusive)
// length of times          1~10^5 (inclusive)
// range of val in times    1~10^9 (inclusive)
// duplicate val?           not known

// intuition
// Min Heap
//      store times in minheap (new int[availalbe timestep, time it needs to take])
//      keep track of current timestep & increment as it process 
// Binary search 
//      sort times
//      binary search between min(times)*n ~ max(times)*n

// import java.util.PriorityQueue;
public class programmers_immigration {
    ///// long min heap -- time limit exceed
    // public long solution(int n, int[] times) {
    //     PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> {
    //         int comp = Long.compare(a[0]+times[(int)a[1]], b[0]+times[(int)b[1]]);
    //         if(comp == 0)
    //             comp = Long.compare(a[0], b[0]);
    //         return comp;
    //     });

    //     for(int i=0; i<times.length; ++i){
    //         // pq.offer(new int[] { 0, times[i] });
    //         pq.offer(new long[] { 0, i }); // in case of duplicate values in times, store indices
    //     }

    //     long ts = 0;
    //     while(n > 0){
    //         long[] curr = pq.poll();

    //         --n;
    //         curr[0] += times[(int)curr[1]];
    //         ts = curr[0];

    //         pq.offer(curr);
    //     }

    //     return ts;
    // }

    public long solution(int n, int[] times) {
        // note that using min=1 instead of sorting the times is much faster! 
        // to perform multiplication of ints and get long as result, must explicitly typecast the operands => long = (long)int*int
        
        // time: O(nlognm) where n is length of arr times and m is max(times)
        int max = 0;
        for(int time: times)
            max = max<time ? time : max;
        long left = 1, right = (long)max*n;
        while(left <= right){
            long mid = left + (right-left)/2;
            int count = 0;
            for(int time : times)
                count += mid/time;
            if(count >= n)
                right = mid-1;
            else
                left = mid+1;
        }

        return left;
    }
}
