//import java.util.Arrays;
//
//object SumTwoNumbers {
//  def main(args: Array[String]): Unit = {
//    val input_array =  Array( -21, 301, 12, 4, 65, 56, 210, 356, 9, -47)
//    println(twoNumberSum(input_array,163).toList)
//
//  }
//
//  def twoNumberSum(array: Array[Int], targetSum: Int ): Array[Int] = {
//    Arrays.sort(array);
//    var left = 0;
//    var right = array.length -1;
//    while (left < right){
//      var currentSum = array(left) + array(right);
//      if (currentSum == targetSum){
//        return Array(array(left), array(right));
//      }
//      else if (currentSum < targetSum){
//        left+=1;
//      }
//      else if (currentSum > targetSum){
//        right-=1;
//      }
//    }
//    return Array()
//  }
//}
//
//
//// output: [-47,210]