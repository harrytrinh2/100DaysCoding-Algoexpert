//// # O(nlogn) time | O(1) space
////---------------------------Solution-------------------------------------
//import java.util.*;
//
//class Main {
//
//  public static void main(String[] args) {
//
//    int[] input_array =  new int[]{ -21, 301, 12, 4, 65, 56, 210, 356, 9, -47};
//    System.out.println(Arrays.toString(twoNumberSum(input_array, 163)));
//
//  }
//
//  public static int[] twoNumberSum(int[] array, int targetSum) {
//    // Write your code here.
//    Arrays.sort(array);
//    int left;
//    left = 0;
//    int right ;
//    right = array.length -1 ;
//    while (left < right ) {
//      int currentSum ;
//      currentSum = array[left] + array[right];
//      if ( currentSum == targetSum){
//        return  new int[] {array[left] , array[right]};
//      }
//
//      else if ( currentSum < targetSum){
//      left+=1;
//      }
//
//      else if ( currentSum > targetSum){
//      right-=1;
//      }
//    }
//    return new int[] {};
//  }
//}
//
//// output: [-47, 210]