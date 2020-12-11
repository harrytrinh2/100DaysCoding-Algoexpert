//// # O(nlogn) time | O(1) space
////---------------------------Solution-------------------------------------
//import java.util.*;
//
//class Main {
//
//  public static void main(String[] args) {
//    int[] input_array =  new int[]{ -21, 301, 12, 4, 65, 56, 210, 356, 9, -47};
//    System.out.println(Arrays.toString(twoNumberSum1(input_array, 163)));
//    System.out.println(Arrays.toString(twoNumberSum2(input_array, 163)));
//}
//
//  public static int[] twoNumberSum1(int[] array, int targetSum){
//      for (int i =0; i < array.length ;i++){
//          int firstNum, secondNum;
//          firstNum = array[i];
//          secondNum = targetSum-firstNum;
//          System.out.println(secondNum);
//          if (Arrays.asList(array).contains(secondNum)){ //not working
//              System.out.println("True");
//              return new int[] {firstNum,secondNum};
//          }
//      }
//      return new int[] {};
//  }
//
//  public static int[] twoNumberSum2(int[] array, int targetSum) {
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
//      else if ( currentSum < targetSum){
//      left+=1;
//      }
//      else {
//      right-=1;
//      }
//    }
//    return new int[] {};
//  }
//}
//
//// output: [-47, 210]