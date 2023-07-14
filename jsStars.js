// function jsStars(number) {
//     for (i = 0; i<number; i++) {
//       console.log('*'.repeat(2*i + 1))
//   }
// }
// number = prompt('숫자를 입력해주세요.');
// jsStars(number);

for (i = 0; i < 10; i++) {
    for (j = 1; j < 10 - i; j++) {
        console.log('&nbsp');
    }
    for (j = 0; j < i * 2 + 1; j++) {
        console.log("*");
    }
    console.log("<br>");
}