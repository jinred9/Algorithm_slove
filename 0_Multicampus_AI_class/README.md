# [multi-it] AI 엔지니어 취업캠프(Python) 2
## N계명
1. list, tuple => 복수형 
2. 변수에 담긴 값/함수가 return 하는 값이 True/False 일 경우 => is_ 로 시작한다 
3. 함수명은 가능하면 동사형 
4. 최대한 explicit(명쾌) 하게 <=> implicit(함축)
5. PEP8 최대한 준수 
6. 주석 열심히 달기


## github 사용법

1. **언제나 브랜치부터 확인하기**(pycharm 우측 하단에 브랜치명)

2. 우리 컴퓨터에서 master 브랜치에 갈 일 전혀 없음!!

3. 리모트 저장소의 최신 내용을 반영한다.
   ```shell
   $ git pull origin master
   ```
   
4. 문제 폴더에 본인 이름으로 `내이름.py` 파일을 만든다.

5. 문제를 푼다.

6. 다 풀었다면 커밋

   ```sh
   # add 전에 내 위치(pwd) 확인
   $ git add .
   $ git commit -m '문제번호'
   ```

   ![image-20230210140121140](README.assets/image-20230210140121140.png)

7. 이후 PUSH

   ```sh
   $ git push origin <내이름>  # <= 절대 git push origin master 하지 않을 것
   ```

   ![image-20230210135613469](README.assets/image-20230210135613469.png)

   ![image-20230210140615795](README.assets/image-20230210140615795.png)

8. PR 생성 이후 Merge (만약 아무것도 할 게 없다고 나온다면, 실제로 반영할 게 없다는 뜻)

   ![image-20230210140743513](README.assets/image-20230210140743513.png)

   ![image-20230210140839871](README.assets/image-20230210140839871.png)

9. Merge Conflict 가 날 경우 본인 이름의 파일 말고 다른 파일을 만져서 문제인 상황. 강사에게 문의하세요