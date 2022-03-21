//注释部分可自动忽略
int main () {
	/*简单写一个上台阶问题*/
	int n = 20;
	int dp[n];
	dp[0] = 1;
	dp[1] = 2;
	for(int i = 2; i < 20;i++){
		dp[i] = dp[i - 1] + dp[i - 2];
	}


	float a = 1.5;
	int i = 1;
	i++;
	i--;
	while(i < n){
		i++;
	}
	return 1;
}

