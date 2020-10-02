//object ValidateSequence {
//  def main(args: Array[String]): Unit = {
//    val array = Array(5,1,22,25,6,-1,8,10);
//    val sequence = Array(1,6,-1,10);
//
//    println(ValidateSubsequence(array,sequence));
//    print(ValidateSubsequenceFor(array,sequence));
//  }
//
//  def ValidateSubsequence (array: Array[Int], sequence: Array[Int]) : Boolean = {
//    var idxArr = 0;
//    var idxSeq = 0;
//    while (idxArr < array.length  && idxSeq < sequence.length){
//      if (array(idxArr) == sequence(idxSeq)){
//        idxSeq+=1;
//      }
//      idxArr+=1;
//    }
//    return idxSeq == sequence.length;
//  }
//
//  def ValidateSubsequenceFor (array: Array[Int], sequence: Array[Int]):Boolean={
//    var idxSeq = 0;
//    for (value <- array){
//      if (idxSeq == sequence.length){
//        return true
//      }
//      if (value == array(idxSeq)){
//        idxSeq+=1;
//      }
//    }
//    return idxSeq == sequence.length;
//  }
//
//}
//
