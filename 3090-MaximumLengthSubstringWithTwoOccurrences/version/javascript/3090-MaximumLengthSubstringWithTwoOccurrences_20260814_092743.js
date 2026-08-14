// Last updated: 8/14/2026, 9:27:43 AM
1var maximumLengthSubstring = function(s) {
2    let count = new Array(26).fill(0);
3    let left = 0;
4    let maxLength = 0;
5
6    for (let right = 0; right < s.length; right++) {
7        let index = s.charCodeAt(right) - 97;
8        count[index]++;
9
10        while (count[index] > 2) {
11            let leftIndex = s.charCodeAt(left) - 97;
12            count[leftIndex]--;
13            left++;
14        }
15
16        maxLength = Math.max(maxLength, right - left + 1);
17    }
18
19    return maxLength;
20};