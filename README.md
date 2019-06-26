# 한국어기초사전 포맷 변환

국립국어원의 한국어기초사전에서 (https://krdict.korean.go.kr/) 다운로드한 XML
데이터를 여러가지 사전 형식으로 변환하는 소스입니다. 여러가지 사전
프로그램에서 사용할 수 있습니다.

## 포맷

* dict.xdxf.dz (XDXF) - GoldenDict 등
* dictd - dictd

## 빌드

make, xsltproc, dictzip이 필요합니다. make를 실행하면 여러가지 포맷의 사전을
만듭니다.

```
$ make
```

## 한국어기초사전의 업스트림 데이터 업데이트

한국어기초사전 사이트에서 모든 단어에 대해 XML 형식으로 다운로드합니다. 그러면
XML 파일이 들어 있는 zip 파일을 다운로드하게 되는데 다음과 같이
update-upstream.py를 이용해 소스코드에 들어 있는 데이터를 업데이트할 수
있습니다. 다운로드한 파일이 .../123456.zip 파일이라고 하면,

$ python3 update-upstream.py .../123456.zip

사이트의 버그 때문에 제공하는 XML에 문제가 있을 수 있습니다. 그러한 경우
가능하면 문제점을 피해가는 코드를 포함합니다. 최근에 다운로드한 데이터로
업데이트해 빌드하는데 문제가 있으면 이슈를 알려 주십시오.

## 기타

이 저작물은 크리에이티브 커먼즈 저작자표시-동일조건변경허락 2.0 대한민국
라이선스에 따라 이용할 수 있습니다. 라이선스 전문을 보려면
https://creativecommons.org/licenses/by-sa/2.0/kr/ 을 방문하거나 다음의 주소로
서면 요청해 주십시오. Creative Commons, PO Box 1866, Mountain View, CA 94042,
USA.
