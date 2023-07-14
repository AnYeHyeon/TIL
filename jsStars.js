number = prompt('숫자를 입력해주세요.');
jsStars(number);

function jsStars (number) {
    for(let i = 1, j = 0; i<=number-1; i++){
        console.log(" ".repeat(number-1-i) + "*".repeat(i + j));
        j++;
    }
}
