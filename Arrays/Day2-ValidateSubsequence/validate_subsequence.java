//import java.util.*;
//
//class Main {
//
//  public static void main(String[] args) {
//    int[] input_array =  new int[]{ 5,1,22,25,6,-1,8,10};
//    int[] input_sequence = new int[]{1,6,-1,10};
//    System.out.println(validateSequence(input_array, input_sequence));
//
//  }
//
//  public static boolean validateSequence(int[] array, int[] sequence) {
//    // Write your code here.
//    int idxArr = 0;
//    int idxSeq = 0;
//    while( idxArr < array.length && idxSeq < sequence.length ){
//      if (array[idxArr] == sequence[idxSeq]){
//        idxSeq +=1;
//      }
//      idxArr+=1;
//    }
//    return idxSeq == sequence.length;
//  }
//}
