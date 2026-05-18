# TestFlight 배포 (Fastlane)

알고핏 iOS 앱(`com.algofit.algofit`)을 **TestFlight**에 올려 내부 테스터가 설치·다운로드할 수 있게 하는 절차입니다. 구현은 [algofit-mobile](https://github.com/algorithm-learning-app/algofit-mobile) 저장소 `apps/mobile/ios/fastlane/`에 있습니다.

## 사전 요구사항

| 항목 | 설명 |
|------|------|
| **Apple Developer Program** | 유료 멤버십 (연 $99). 팀에 앱 등록·서명·TestFlight 권한 필요 |
| **App Store Connect 앱** | [App Store Connect](https://appstoreconnect.apple.com) → **앱** → **+** 로 iOS 앱 생성. 번들 ID `com.algofit.algofit`와 일치 |
| **Mac + Xcode** | 최신 Xcode, Command Line Tools. `flutter doctor` iOS 항목 통과 |
| **Flutter** | `apps/mobile`에서 `flutter pub get` 가능한 환경 |
| **Ruby + Bundler** | `cd apps/mobile/ios && bundle install` |

## App Store Connect에서 할 일 (최초 1회)

1. **Identifiers** ([developer.apple.com](https://developer.apple.com/account/resources/identifiers/list))  
   - App ID `com.algofit.algofit` 등록 (없으면 생성).

2. **App Store Connect → 앱**  
   - 새 앱: 플랫폼 iOS, 이름·번들 ID `com.algofit.algofit`, SKU 임의.

3. **TestFlight → 내부 테스팅**  
   - 팀 멤버(App Store Connect Users)는 자동으로 내부 테스터.  
   - **내부 그룹**에 빌드가 처리되면(Processing 완료) 테스터에게 표시됩니다.  
   - iPhone **TestFlight** 앱에서 초대 수락 후 설치·다운로드.

4. **인증서·프로비저닝 (배포용)**  
   - **자동 서명**: Xcode에서 Runner 타깃 Release + Team 선택 후 한 번 Archive 성공하면, `flutter build ipa`가 같은 팀으로 서명 가능.  
   - **수동 / 팀 공유**: [fastlane match](https://docs.fastlane.tools/actions/match/) 권장  
     ```bash
     cd apps/mobile/ios
     bundle exec fastlane match appstore
     ```  
     (별도 git 저장소에 인증서 보관 — 시크릿 저장소 필수)

## App Store Connect API 키 (권장, 비대화형)

1. App Store Connect → **사용자 및 액세스** → **키** → **App Store Connect API** → 키 생성 (역할: **앱 관리** 이상).
2. `.p8` 파일을 **한 번만** 다운로드 — 저장소에 커밋하지 마세요.
3. 환경 변수:

| 변수 | 설명 |
|------|------|
| `APP_STORE_CONNECT_API_KEY_ID` | Key ID (예: `ABC123XYZ`) |
| `APP_STORE_CONNECT_ISSUER_ID` | Issuer ID (사용자 및 액세스 페이지 상단 UUID) |
| `APP_STORE_CONNECT_API_KEY_PATH` | `.p8` 파일 **절대 경로** |

예시 (`ios/fastlane/.env.example` 참고):

```bash
export DEVELOPMENT_TEAM="XXXXXXXXXX"
export APP_STORE_CONNECT_API_KEY_ID="..."
export APP_STORE_CONNECT_ISSUER_ID="..."
export APP_STORE_CONNECT_API_KEY_PATH="$HOME/.private/AuthKey_XXXXXX.p8"
```

## 대안: Apple ID + 앱 전용 암호

- `FASTLANE_APPLE_ID`, `FASTLANE_PASSWORD`(또는 `FASTLANE_APPLE_APPLICATION_SPECIFIC_PASSWORD`)  
- CI/스크립트에서는 **API 키 방식을 권장**합니다. Apple ID 로그인은 대화형 세션이 필요할 수 있습니다.

## 로컬 명령

```bash
cd apps/mobile/ios
bundle install

# IPA만 빌드 (업로드 없음)
bundle exec fastlane build

# IPA 빌드 + TestFlight 업로드
bundle exec fastlane beta
```

- `build` / `beta` 모두 프로젝트 루트(`apps/mobile`)에서 `flutter build ipa --release` 실행.  
- 산출물: `apps/mobile/build/ios/ipa/*.ipa`  
- `beta`는 `upload_to_testflight`로 업로드 후, App Store Connect에서 처리·내부 테스터 배포.

## 환경 변수 요약

| 변수 | 필수 | 용도 |
|------|------|------|
| `DEVELOPMENT_TEAM` 또는 `FASTLANE_TEAM_ID` | 서명 시 권장 | Apple Developer Team ID |
| `APP_STORE_CONNECT_API_KEY_*` | `beta` 업로드 시 권장 | API 키 인증 |
| `FASTLANE_APPLE_ID` 등 | API 키 없을 때 | Apple ID 업로드 (대화형 가능) |

## PR·검증

- 브랜치: `feat/fastlane-testflight` → `main` PR.  
- [algofit-mobile](https://github.com/algorithm-learning-app/algofit-mobile) `scripts/pr-review-check.sh`: `flutter analyze` · `flutter test` (Fastlane은 PR 체크에 포함되지 않음).

## 수출 관리 (Export Compliance)

앱이 **표준 HTTPS/TLS**만 사용하고 자체 암호화·비표준 암호화를 제공하지 않으면, 미국 수출 규정상 **면제(exempt)** 대상입니다.

| 위치 | 설정 |
|------|------|
| **Info.plist** (iOS·macOS `Runner`) | `ITSAppUsesNonExemptEncryption` = `false` |
| **Fastlane** `upload_to_testflight` | `uses_non_exempt_encryption: false` |
| **App Store Connect** (빌드별 질문) | “앱이 암호화를 사용합니까?” → **아니오** (또는 면제 해당 시 동일 의미) |

빌드 업로드 후 ASC에서 수출 규정 설문이 뜨면, 위 plist·Fastlane 설정과 같이 **비면제 암호화 없음**으로 답하면 됩니다.

## 보안

- `.p8`, `fastlane/.env`, API 키·앱 전용 암호 **커밋 금지**.  
- `.gitignore`에 `*.p8`, `AuthKey_*.p8`, `fastlane/.env` 등 등록됨.

## 관련 문서

- [20-pr-review-setup.md](20-pr-review-setup.md) — PR 로컬 봇  
- [21-git-workflow.md](21-git-workflow.md) — feature 브랜치·머지  
- [algofit-mobile README](https://github.com/algorithm-learning-app/algofit-mobile/blob/main/README.md) — TestFlight 링크
