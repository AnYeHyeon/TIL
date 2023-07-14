int start_4 = 5/2; // 별의 시작 점 ( 중간부터 시작, n / 2 )
        int end_4 = 5/2;   // 별의 끝나는 점 ( 중간부터 시작, n / 2 )

        for(int i = 0 ; i<4 ; i++) {         //행의 수
            for(int j = 0 ; j<5 ; j++) {    //열의 수
                if(j>start_4 && j<end_4) {    // j가 start 보다 크고 end보다 작으면 * 아니면 공백
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            start_4--; // start를 감소시키고 end를 증가시켜서 *을 넓게 찍는다.
            end_4++;
            System.out.println();
        }