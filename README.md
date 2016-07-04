Using the techniques in [How to Project Customer Retention](https://marketing.wharton.upenn.edu/files/?whdmsaction=public:main.file&fileID=327) by Fader & Hardie (2006), and an implementation of those techniques by [JD Maturen](https://github.com/jdmaturen), Retentionizer will fit a shifted-beta-geometric distribution to the data, show the projected retention rates for each cohort, show the imputed beta distribution for each cohort, and calculate the LTV of a given customer in that cohort.

Basically, it turns a sample of cohort survival rates:

| t  | past 30 |
|----|---------|
| 0  | 1.0     |
| 1  | .81     |
| 2  | .80     |
| 3  | .76     |
| 4  | .75     |
| 5  | .72     |
| 6  | .70     |
| 7  | .67     |
| 8  | .66     |
| 9  | .65     |
| 10 | .64     |

Into this:

![sample-output](https://raw.githubusercontent.com/chrisclark/retentionizer/master/static/img/sample-output.png)

Retentionizer is built by [David Chudzicki](https://www.github.com/dchudz) and [Chris Clark](https://blog.untrod.com/).
