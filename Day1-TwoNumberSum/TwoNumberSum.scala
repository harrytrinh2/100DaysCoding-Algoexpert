import java.util._;

object SumTwoNumbers {
  def main(args: Array[String]): Unit = {
    val array = Array(1,5,2,11,-3,1,2,9);
    println(sumTwoNumbers(array,16).toList)
  }


  def twoNumberSum(array: Array[Int], targetSum: Int ): Array[Int] = {
      var left = 0;
      var right = array.length -1;
      var currentSum = array(left) + array(right);
      while (left < right){
        if (currentSum == targetSum){
          return Array(array(left), array(right));
        }
        else if (currentSum < targetSum){
          left+=1;
        }
        else if (currentSum > targetSum){
          right-=1;
        }
      }
      return Array()
  }
}

