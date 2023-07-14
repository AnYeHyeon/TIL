function jsStars(number) {
    for (i = 0; i<number; i++) {
      console.log('*'.repeat(2*i + 1))
  }
}

number = prompt('숫자를 입력해주세요.');
jsStars(number);