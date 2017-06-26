function rot13(str) { // LBH QVQ VG!
  //匹配所有的大写字母
  var result = str.replace(/[A-Z]/g, function (s) {
    //获取其ascci码
    var c = s.charCodeAt(0);
    //N-Z
    if (c >= 78 && c <= 90) {
      return String.fromCharCode(c - 13);
    } else { //A-M
      return String.fromCharCode(c + 13);
    }
  });
  return result;
}

// Change the inputs below to test
rot13("SERR PBQR PNZC");