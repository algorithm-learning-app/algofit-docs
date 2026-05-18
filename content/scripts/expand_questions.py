#!/usr/bin/env python3
"""Expand pick.json to 80+ and blank.json to 50+ with multi-language blanks."""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PICK_PATH = ROOT / "content/questions/pick.json"
BLANK_PATH = ROOT / "content/questions/blank.json"

SYNC_DIRS = [
    ROOT / "apps/mobile/assets/data",
    ROOT / "apps/web/src/content",
    ROOT / "_repos/algofit-docs/content/questions",
]

ID_PATTERN = re.compile(r"^(pick|blank|scenario)_[a-z0-9_]+$")


def pick(
    id: str,
    stem: str,
    tags: list[str],
    difficulty: int,
    choices: list[tuple[str, str]],
    correct: str,
    explanation: str,
) -> dict:
    return {
        "id": id,
        "type": "pick",
        "version": 1,
        "language": "python",
        "stem": stem,
        "tags": tags,
        "difficulty": difficulty,
        "choices": [{"id": cid, "label": label} for cid, label in choices],
        "correctChoiceId": correct,
        "explanation": explanation,
    }


def blank(
    id: str,
    stem: str,
    tags: list[str],
    difficulty: int,
    code: str,
    slots: list[dict],
    explanation: str,
    language: str = "python",
) -> dict:
    return {
        "id": id,
        "type": "blank",
        "version": 1,
        "language": language,
        "stem": stem,
        "tags": tags,
        "difficulty": difficulty,
        "codeTemplate": code,
        "blanks": slots,
        "explanation": explanation,
    }


def slot(bid: str, correct: list[str], choices: list[str]) -> dict:
    return {"id": bid, "correctAnswers": correct, "choices": choices}


EXTRA_PICKS = [
    pick(
        "pick_sort_001",
        "정수 배열을 **오름차순**으로 정렬할 때, 평균 O(n log n)이 보장되는 비교 기반 정렬로 가장 흔히 쓰는 것은?",
        ["sorting"],
        1,
        [
            ("c1", "병합·퀵·힙 정렬 등 O(n log n)"),
            ("c2", "버블 정렬만 항상 최적"),
            ("c3", "BFS로 최단 경로"),
            ("c4", "해시로 two-sum만"),
        ],
        "c1",
        "일반 목적 정렬은 merge/quick/heap이 O(n log n)입니다. 버블은 최악 O(n²)이고 BFS·해시는 정렬과 무관합니다.",
    ),
    pick(
        "pick_sort_002",
        "거의 정렬된 배열을 **in-place**로 빠르게 정렬하려 합니다. 인접 원소를 교환하며 early stop하는 단순 방법은?",
        ["sorting"],
        2,
        [
            ("c1", "삽입 정렬(insertion sort)"),
            ("c2", "이분 탐색만"),
            ("c3", "단조 스택 NGE"),
            ("c4", "multi-source BFS"),
        ],
        "c1",
        "삽입 정렬은 거의 정렬된 입력에서 빠르게 동작합니다. 이분·스택·BFS는 정렬 알고리즘이 아닙니다.",
    ),
    pick(
        "pick_dp_001",
        "피보나치 F(n)을 **중복 계산 없이** O(n)에 구하려면, 이전 값을 배열에 저장하는 방식은?",
        ["dp"],
        2,
        [
            ("c1", "바텀업 DP(테이블 채우기)"),
            ("c2", "BFS 큐만"),
            ("c3", "투 포인터 merge"),
            ("c4", "스택으로 괄호만"),
        ],
        "c1",
        "피보나치 DP는 작은 부분 문제를 순서대로 채웁니다. BFS·merge·스택은 수열 DP와 다릅니다.",
    ),
    pick(
        "pick_dp_002",
        "계단을 한 번에 1 또는 2칸 오를 때 **도달 방법의 수**를 구합니다. 마지막 칸 직전 상태 두 가지를 더하는 점화식은?",
        ["dp"],
        2,
        [
            ("c1", "dp[i] = dp[i-1] + dp[i-2]"),
            ("c2", "dp[i] = dp[i-1] * dp[i-2]"),
            ("c3", "BFS로 레벨만"),
            ("c4", "이분 탐색 lower bound"),
        ],
        "c1",
        "계단 오르기는 피보나치형 DP입니다. 곱·BFS·이분은 방법 수 점화와 맞지 않습니다.",
    ),
    pick(
        "pick_greedy_001",
        "회의실 배정: 종료 시각이 빠른 회의부터 골라 겹치지 않게 최대 개수를 구할 때 쓰는 전략은?",
        ["greedy"],
        2,
        [
            ("c1", "종료 시각 기준 정렬 후 greedy 선택"),
            ("c2", "모든 부분집합 brute force만"),
            ("c3", "BFS 최단 경로"),
            ("c4", "prefix 해시만"),
        ],
        "c1",
        "interval scheduling은 end time greedy가 표준입니다. brute·BFS·prefix만으로는 최적 greedy가 아닙니다.",
    ),
    pick(
        "pick_greedy_002",
        "동전 거스름돈에서 **항상 큰 동전부터** 고르면 최적이 보장되지 않을 수 있습니다. 반면 특정 동전 체계(예: 1,5,10,25)에서는?",
        ["greedy"],
        2,
        [
            ("c1", "greedy가 최적인 특수 케이스(캐노니컬)"),
            ("c2", "항상 DP가 불필요"),
            ("c3", "BFS만으로 충분"),
            ("c4", "스택 LIFO만"),
        ],
        "c1",
        "일반 동전 문제는 DP가 필요할 수 있고, 특정 액면가 체계에서만 greedy가 맞습니다.",
    ),
    pick(
        "pick_ll_001",
        "단일 연결 리스트에서 **사이클 존재 여부**를 O(1) 추가 공간에 검사하려면?",
        ["linked_list"],
        2,
        [
            ("c1", "느린·빠른 포인터(Floyd)"),
            ("c2", "해시로 two-sum"),
            ("c3", "이분 탐색만"),
            ("c4", "스택으로 괄호"),
        ],
        "c1",
        "사이클 검사는 slow/fast pointer가 전형입니다. two-sum·이분·괄호 스택은 리스트 사이클과 무관합니다.",
    ),
    pick(
        "pick_ll_002",
        "정렬된 두 연결 리스트를 **병합**할 때, 더미 노드 뒤에 작은 값을 연결하는 방식은?",
        ["linked_list"],
        2,
        [
            ("c1", "두 포인터로 merge"),
            ("c2", "BFS 레벨 순회"),
            ("c3", "단조 스택 NGE"),
            ("c4", "prefix sum 해시만"),
        ],
        "c1",
        "sorted list merge는 array merge와 같은 two-pointer 패턴입니다.",
    ),
    pick(
        "pick_rec_001",
        "트리의 **최대 깊이**를 구할 때, 자식 재귀 결과에 1을 더하는 구조는?",
        ["recursion"],
        1,
        [
            ("c1", "재귀 + base case(리프는 0 또는 1)"),
            ("c2", "투 포인터 3-sum"),
            ("c3", "해시 two-sum만"),
            ("c4", "BFS 없이 스택만 필수"),
        ],
        "c1",
        "트리 깊이는 전형적인 재귀 정의입니다. 3-sum·two-sum·스택만은 깊이 정의와 다릅니다.",
    ),
    pick(
        "pick_rec_002",
        "순열/조합을 **백트래킹**으로 생성할 때, 선택을 취소(unchoose)하는 이유는?",
        ["recursion"],
        2,
        [
            ("c1", "다른 가지 탐색을 위해 상태를 되돌림"),
            ("c2", "최단 거리 보장"),
            ("c3", "O(log n) 정렬만"),
            ("c4", "해시 충돌 처리"),
        ],
        "c1",
        "백트래킹은 choose-explore-unchoose입니다. 최단거리·정렬·해시 충돌과는 무관합니다.",
    ),
    pick(
        "pick_tree_001",
        "이진 탐색 트리에서 **중위 순회(inorder)** 결과는?",
        ["tree"],
        2,
        [
            ("c1", "키 오름차순(정렬된 순서)"),
            ("c2", "레벨 순서"),
            ("c3", "무작위 순서"),
            ("c4", "루트만 출력"),
        ],
        "c1",
        "BST inorder는 정렬 순서를 줍니다. level order는 BFS, 나머지는 inorder 정의가 아닙니다.",
    ),
    pick(
        "pick_tree_002",
        "트리의 **레벨 순회**에 쓰는 자료구조는?",
        ["tree", "bfs"],
        1,
        [
            ("c1", "큐(BFS)"),
            ("c2", "스택만(DFS preorder와 동일)"),
            ("c3", "해시 맵만"),
            ("c4", "이분 탐색"),
        ],
        "c1",
        "레벨 순회는 BFS 큐입니다. 스택 DFS는 깊이 우선이고 level order와 다릅니다.",
    ),
    pick(
        "pick_heap_001",
        "실시간으로 **최댓값/최솟값**을 삽입·삭제하려면 평균 O(log n)인 구조는?",
        ["heap"],
        2,
        [
            ("c1", "힙(priority queue)"),
            ("c2", "단일 연결 리스트만"),
            ("c3", "투 포인터 merge"),
            ("c4", "스택 LIFO"),
        ],
        "c1",
        "우선순위 큐/힙이 동적 min/max에 적합합니다.",
    ),
    pick(
        "pick_heap_002",
        "배열에서 **K번째 큰 원소**를 평균 O(n)에 찾는 방법은?",
        ["heap"],
        3,
        [
            ("c1", "quickselect(분할)"),
            ("c2", "버블 정렬 전체"),
            ("c3", "BFS만"),
            ("c4", "괄호 스택만"),
        ],
        "c1",
        "Kth element는 quickselect 또는 size-k heap이 표준입니다.",
    ),
    pick(
        "pick_sliding_001",
        "고정 길이 k인 **슬라이딩 윈도우 최댓값**을 각 위치마다 구할 때 deque로 front를 관리하는 알고리즘은?",
        ["two_pointer"],
        3,
        [
            ("c1", "단조 deque(sliding window maximum)"),
            ("c2", "이분 탐색 sqrt"),
            ("c3", "BFS multi-source"),
            ("c4", "해시 anagram만"),
        ],
        "c1",
        "Sliding window max는 monotonic deque가 O(n) 해법입니다.",
    ),
    pick(
        "pick_sliding_002",
        "문자열에서 **길이 k 부분 문자열**이 모두 다른지 확인하려면?",
        ["hash", "two_pointer"],
        2,
        [
            ("c1", "윈도우 + set/해시로 중복 검사"),
            ("c2", "스택 DFS만"),
            ("c3", "이분 lower bound"),
            ("c4", "BFS 격자만"),
        ],
        "c1",
        "고정 k 윈도우는 set/해시로 O(n)에 중복을 검사합니다.",
    ),
    pick(
        "pick_math_001",
        "1부터 n까지 합을 O(1)에 구하는 공식은?",
        ["math"],
        1,
        [
            ("c1", "n * (n + 1) / 2"),
            ("c2", "n * (n - 1)"),
            ("c3", "2^n"),
            ("c4", "n log n"),
        ],
        "c1",
        "등차수열 합 공식 n(n+1)/2입니다.",
    ),
    pick(
        "pick_math_002",
        "소수 판별을 **√n까지** 나눠 보는 방식의 시간 복잡도는?",
        ["math"],
        1,
        [
            ("c1", "O(√n)"),
            ("c2", "O(1)"),
            ("c3", "O(n log n)"),
            ("c4", "O(log log n)만 항상"),
        ],
        "c1",
        "trial division은 √n까지 검사합니다.",
    ),
    pick(
        "pick_graph_001",
        "가중치 있는 그래프 **최단 경로(음수 간선 없음)** 에 Dijkstra가 쓰는 구조는?",
        ["graph"],
        3,
        [
            ("c1", "우선순위 큐(힙) + 거리 갱신"),
            ("c2", "스택 LIFO만"),
            ("c3", "투 포인터만"),
            ("c4", "버블 정렬"),
        ],
        "c1",
        "Dijkstra는 min-heap으로 확장합니다.",
    ),
    pick(
        "pick_graph_002",
        "무방향 그래프의 **연결 요소 개수**를 세려면?",
        ["graph", "bfs"],
        2,
        [
            ("c1", "BFS/DFS로 미방문 정점 탐색"),
            ("c2", "이분 탐색만"),
            ("c3", "단조 스택만"),
            ("c4", "3-sum 투 포인터"),
        ],
        "c1",
        "연결 요소는 그래프 탐색으로 셉니다.",
    ),
    pick(
        "pick_bit_001",
        "짝수 여부를 **비트 연산** 한 번으로 검사하려면?",
        ["bit"],
        1,
        [
            ("c1", "n & 1 == 0"),
            ("c2", "n >> 2 == 0"),
            ("c3", "n | 1 == 0"),
            ("c4", "n ^ n == 1"),
        ],
        "c1",
        "최하위 비트가 0이면 짝수입니다.",
    ),
    pick(
        "pick_bit_002",
        "두 정수의 **XOR**은 같은 비트 위치가 다를 때 1이 됩니다. a ^ a의 결과는?",
        ["bit"],
        1,
        [
            ("c1", "0"),
            ("c2", "1"),
            ("c3", "a"),
            ("c4", "2a"),
        ],
        "c1",
        "같은 값 XOR은 0입니다.",
    ),
    pick(
        "pick_str_001",
        "문자열이 **회문**인지 양끝 포인터로 검사하는 패턴은?",
        ["two_pointer"],
        1,
        [
            ("c1", "투 포인터로 안쪽으로 비교"),
            ("c2", "BFS 큐만"),
            ("c3", "이분 탐색 lower bound"),
            ("c4", "스택 NGE"),
        ],
        "c1",
        "회문 검사는 양끝 two pointer가 기본입니다.",
    ),
    pick(
        "pick_str_002",
        "문자열 **압축 길이**(연속 동일 문자 개수)를 세려면?",
        ["array"],
        1,
        [
            ("c1", "한 번 순회하며 run length 세기"),
            ("c2", "BFS만"),
            ("c3", "이분만"),
            ("c4", "해시 3-sum"),
        ],
        "c1",
        "run-length는 단일 패스로 처리합니다.",
    ),
    pick(
        "pick_design_001",
        "LRU 캐시를 O(1) get/put으로 구현할 때 흔히 쓰는 조합은?",
        ["design"],
        3,
        [
            ("c1", "해시맵 + 이중 연결 리스트"),
            ("c2", "스택만"),
            ("c3", "버블 정렬"),
            ("c4", "BFS만"),
        ],
        "c1",
        "LRU는 hash map + DLL이 표준입니다.",
    ),
    pick(
        "pick_design_002",
        "스택의 push/pop을 **큐**처럼 사용하려면?",
        ["design", "stack"],
        2,
        [
            ("c1", "스택 두 개(in/out)"),
            ("c2", "힙 하나만"),
            ("c3", "이분 탐색"),
            ("c4", "BFS deque 없이"),
        ],
        "c1",
        "Queue via two stacks가 클래식입니다.",
    ),
    pick(
        "pick_sim_001",
        "시뮬레이션: 격자에서 **방향 배열**로 이동할 때 경계를 벗어나면?",
        ["simulation"],
        1,
        [
            ("c1", "조건문으로 범위 검사 후 스킵/중단"),
            ("c2", "무조건 wrap-around"),
            ("c3", "이분 탐색"),
            ("c4", "해시 two-sum"),
        ],
        "c1",
        "격자 시뮬레이션은 bounds check가 필수입니다.",
    ),
    pick(
        "pick_sim_002",
        "로봇 청소기가 **장애물까지 직진** 후 회전하는 규칙을 코드로 옮기면?",
        ["simulation"],
        2,
        [
            ("c1", "방향 벡터 + while 이동 시뮬레이션"),
            ("c2", "DP 테이블만"),
            ("c3", "merge sort"),
            ("c4", "topological sort만"),
        ],
        "c1",
        "규칙 기반 이동은 시뮬레이션 루프로 구현합니다.",
    ),
    pick(
        "pick_review_001",
        "복습 큐에 **최근 오답**을 넣고 간격을 늘리는 학습 전략과 가장 가까운 것은?",
        ["review"],
        1,
        [
            ("c1", "간격 반복(spaced repetition)"),
            ("c2", "이분 탐색만"),
            ("c3", "BFS만"),
            ("c4", "greedy coin 항상"),
        ],
        "c1",
        "오답 복습은 spaced repetition 개념과 맞습니다.",
    ),
    pick(
        "pick_review_002",
        "같은 패턴 태그 문제를 연속으로 풀 때 기대 효과는?",
        ["review"],
        1,
        [
            ("c1", "패턴 인식 강화"),
            ("c2", "메모리 사용 0"),
            ("c3", "O(1) 정렬 보장"),
            ("c4", "그래프 사이클 제거"),
        ],
        "c1",
        "태그별 연습은 패턴 매칭 능력을 키웁니다.",
    ),
    pick(
        "pick_mix_001",
        "정렬된 배열에서 **중복 제거(in-place)** 후 길이를 반환할 때 투 포인터 역할은?",
        ["array", "two_pointer"],
        2,
        [
            ("c1", "쓰기 포인터 + 읽기 포인터"),
            ("c2", "BFS parent만"),
            ("c3", "스택 NGE"),
            ("c4", "Dijkstra heap"),
        ],
        "c1",
        "in-place unique는 slow/fast write 패턴입니다.",
    ),
    pick(
        "pick_mix_002",
        "**부분집합 합**이 target인지 보려면 정렬 후 투 포인터 또는?",
        ["two_pointer", "hash"],
        2,
        [
            ("c1", "해시 set으로 complement 탐색"),
            ("c2", "BFS만"),
            ("c3", "괄호 스택"),
            ("c4", "topo sort"),
        ],
        "c1",
        "subset sum 변형은 해시/투 포인터 조합이 흔합니다.",
    ),
]

MULTI_LANG_BLANKS = [
    blank(
        "blank_java_bs_001",
        "정렬된 배열에서 target의 인덱스를 찾는 **Java 이분 탐색**입니다. 빈칸을 채우세요.",
        ["binary_search"],
        2,
        "int search(int[] nums, int target) {\n    int left = 0, right = nums.length - 1;\n    while ({{b1}}) {\n        int mid = left + (right - left) / 2;\n        if (nums[mid] == target) return mid;\n        else if (nums[mid] < target) {{b2}}\n        else right = mid - 1;\n    }\n    return -1;\n}",
        [
            slot("b1", ["left <= right"], ["left <= right", "left < right", "mid <= right", "left != right"]),
            slot("b2", ["left = mid + 1"], ["left = mid + 1", "left = mid", "right = mid + 1", "left--"]),
        ],
        "while은 left <= right이고, target이 더 크면 left를 mid+1로 올립니다.",
        language="java",
    ),
    blank(
        "blank_java_tp_001",
        "Java에서 정렬 배열 **두 수의 합**을 투 포인터로 찾습니다. 빈칸을 채우세요.",
        ["two_pointer"],
        2,
        "int[] twoSumSorted(int[] nums, int target) {\n    int left = 0, right = nums.length - 1;\n    while (left < right) {\n        int sum = nums[left] + nums[right];\n        if (sum == target) return new int[]{left, right};\n        else if (sum < target) {{b1}}\n        else right--;\n    }\n    return new int[]{-1, -1};\n}",
        [slot("b1", ["left++"], ["left++", "left--", "right++", "left = right"])],
        "합이 작으면 left를 증가시켜 더 큰 합을 만듭니다.",
        language="java",
    ),
    blank(
        "blank_java_hash_001",
        "Java **HashMap**으로 문자 빈도를 셉니다. 빈칸을 채우세요.",
        ["hash"],
        1,
        "Map<Character, Integer> freq(char[] s) {\n    Map<Character, Integer> map = new HashMap<>();\n    for (char ch : s) {\n        {{b1}}\n    }\n    return map;\n}",
        [
            slot(
                "b1",
                ["map.put(ch, map.getOrDefault(ch, 0) + 1)"],
                [
                    "map.put(ch, map.getOrDefault(ch, 0) + 1)",
                    "map.put(ch, 1)",
                    "map.remove(ch)",
                    "map.clear()",
                ],
            )
        ],
        "getOrDefault로 기존 빈도에 1을 더합니다.",
        language="java",
    ),
    blank(
        "blank_java_stack_001",
        "Java **Stack**으로 괄호 유효성을 검사합니다. 빈칸을 채우세요.",
        ["stack"],
        1,
        "boolean isValid(String s) {\n    Deque<Character> st = new ArrayDeque<>();\n    for (char ch : s.toCharArray()) {\n        if (ch == '(' || ch == '[' || ch == '{') st.push(ch);\n        else if (st.isEmpty()) return false;\n        else {{b1}}\n    }\n    return st.isEmpty();\n}",
        [slot("b1", ["st.pop()"], ["st.pop()", "st.push(ch)", "st.peek()", "return true"])],
        "닫는 괄호면 짝이 맞는지 확인 후 pop합니다.",
        language="java",
    ),
    blank(
        "blank_java_arr_001",
        "Java에서 배열 **최댓값**을 순회하며 구합니다. 빈칸을 채우세요.",
        ["array"],
        1,
        "int max(int[] nums) {\n    int best = Integer.MIN_VALUE;\n    for (int x : {{b1}}) {\n        if (x > best) best = x;\n    }\n    return best;\n}",
        [slot("b1", ["nums"], ["nums", "nums.length", "best", "x"])],
        "향상된 for는 nums를 직접 순회합니다.",
        language="java",
    ),
    blank(
        "blank_java_bfs_001",
        "Java **Queue**로 BFS를 시작합니다. 빈칸을 채우세요.",
        ["bfs"],
        2,
        "void bfs(int start, List<List<Integer>> adj) {\n    Queue<Integer> q = new ArrayDeque<>();\n    boolean[] seen = new boolean[adj.size()];\n    q.offer(start);\n    seen[start] = true;\n    while (!q.isEmpty()) {\n        int u = {{b1}};\n        for (int v : adj.get(u)) {\n            if (!seen[v]) {\n                seen[v] = true;\n                q.offer(v);\n            }\n        }\n    }\n}",
        [slot("b1", ["q.poll()"], ["q.poll()", "q.peek()", "q.offer(u)", "q.clear()"])],
        "BFS는 큐 front를 poll로 꺼냅니다.",
        language="java",
    ),
    blank(
        "blank_java_sort_001",
        "Java **Arrays.sort**로 정렬합니다. 빈칸을 채우세요.",
        ["sorting"],
        1,
        "void sortAsc(int[] nums) {\n    {{b1}}\n}",
        [
            slot(
                "b1",
                ["Arrays.sort(nums)"],
                ["Arrays.sort(nums)", "nums.sort()", "Collections.sort(nums)", "Arrays.reverse(nums)"],
            )
        ],
        "원시 배열 int[]는 Arrays.sort를 씁니다.",
        language="java",
    ),
    blank(
        "blank_java_ll_001",
        "Java에서 연결 리스트를 **역순**으로 바꿉니다. 빈칸을 채우세요.",
        ["linked_list"],
        2,
        "ListNode reverse(ListNode head) {\n    ListNode prev = null, cur = head;\n    while (cur != null) {\n        ListNode next = cur.next;\n        cur.next = prev;\n        prev = cur;\n        {{b1}}\n    }\n    return prev;\n}",
        [slot("b1", ["cur = next"], ["cur = next", "cur = prev", "prev = next", "return cur"])],
        "다음 노드를 저장한 뒤 cur를 next로 전진합니다.",
        language="java",
    ),
    blank(
        "blank_js_bs_001",
        "JavaScript **이분 탐색**입니다. 빈칸을 채우세요.",
        ["binary_search"],
        2,
        "function search(nums, target) {\n  let left = 0, right = nums.length - 1;\n  while ({{b1}}) {\n    const mid = Math.floor((left + right) / 2);\n    if (nums[mid] === target) return mid;\n    if (nums[mid] < target) {{b2}}\n    else right = mid - 1;\n  }\n  return -1;\n}",
        [
            slot("b1", ["left <= right"], ["left <= right", "left < right", "mid <= right", "left !== right"]),
            slot("b2", ["left = mid + 1"], ["left = mid + 1", "left = mid", "right = mid + 1", "left--"]),
        ],
        "while 조건과 target이 클 때 left 이동이 핵심입니다.",
        language="javascript",
    ),
    blank(
        "blank_js_tp_001",
        "JavaScript **투 포인터**로 두 수의 합을 찾습니다. 빈칸을 채우세요.",
        ["two_pointer"],
        2,
        "function twoSumSorted(nums, target) {\n  let left = 0, right = nums.length - 1;\n  while (left < right) {\n    const sum = nums[left] + nums[right];\n    if (sum === target) return [left, right];\n    if (sum < target) {{b1}}\n    else right--;\n  }\n  return [-1, -1];\n}",
        [slot("b1", ["left++"], ["left++", "left--", "right++", "left = right"])],
        "합이 작으면 left를 올립니다.",
        language="javascript",
    ),
    blank(
        "blank_js_hash_001",
        "JavaScript **Map**으로 빈도를 셉니다. 빈칸을 채우세요.",
        ["hash"],
        1,
        "function freq(s) {\n  const map = new Map();\n  for (const ch of s) {\n    {{b1}}\n  }\n  return map;\n}",
        [
            slot(
                "b1",
                ["map.set(ch, (map.get(ch) ?? 0) + 1)"],
                [
                    "map.set(ch, (map.get(ch) ?? 0) + 1)",
                    "map.delete(ch)",
                    "map.clear()",
                    "map.set(ch, ch)",
                ],
            )
        ],
        "get 후 null 병합으로 +1합니다.",
        language="javascript",
    ),
    blank(
        "blank_js_arr_001",
        "JavaScript에서 배열 **filter**로 짝수만 고릅니다. 빈칸을 채우세요.",
        ["array"],
        1,
        "function pickEvens(nums) {\n  return nums.filter(x => {{b1}});\n}",
        [slot("b1", ["x % 2 === 0"], ["x % 2 === 0", "x % 2", "x > 0", "x === 1"])],
        "짝수는 x % 2 === 0입니다.",
        language="javascript",
    ),
    blank(
        "blank_js_stack_001",
        "JavaScript **스택(배열)**으로 괄호를 검사합니다. 빈칸을 채우세요.",
        ["stack"],
        1,
        "function isValid(s) {\n  const st = [];\n  for (const ch of s) {\n    if ('([{'.includes(ch)) st.push(ch);\n    else if ({{b1}}) return false;\n    else st.pop();\n  }\n  return st.length === 0;\n}",
        [slot("b1", ["st.length === 0"], ["st.length === 0", "st.length > 0", "ch === st[0]", "st.push(ch)"])],
        "닫는 괄호인데 스택이 비면 false입니다.",
        language="javascript",
    ),
    blank(
        "blank_js_bfs_001",
        "JavaScript **큐**로 BFS를 돕니다. 빈칸을 채우세요.",
        ["bfs"],
        2,
        "function bfs(start, adj) {\n  const q = [start];\n  const seen = new Set([start]);\n  while (q.length) {\n    const u = {{b1}};\n    for (const v of adj[u]) {\n      if (!seen.has(v)) {\n        seen.add(v);\n        q.push(v);\n      }\n    }\n  }\n}",
        [slot("b1", ["q.shift()"], ["q.shift()", "q.pop()", "q.push(u)", "q.clear()"])],
        "FIFO는 shift로 front를 꺼냅니다.",
        language="javascript",
    ),
    blank(
        "blank_js_async_001",
        "JavaScript에서 **Promise** 결과를 기다립니다. 빈칸을 채우세요.",
        ["async"],
        1,
        "async function load() {\n  const data = {{b1}} fetch(url);\n  return data.json();\n}",
        [slot("b1", ["await"], ["await", "async", "return", "new"])],
        "비동기 결과는 await로 기다립니다.",
        language="javascript",
    ),
    blank(
        "blank_js_reduce_001",
        "JavaScript **reduce**로 합을 구합니다. 빈칸을 채우세요.",
        ["array"],
        1,
        "function sum(nums) {\n  return nums.reduce((acc, x) => {{b1}}, 0);\n}",
        [slot("b1", ["acc + x"], ["acc + x", "acc * x", "x - acc", "acc"])],
        "누적값 acc에 x를 더합니다.",
        language="javascript",
    ),
    blank(
        "blank_c_bs_001",
        "C 언어 **이분 탐색** while 조건입니다. 빈칸을 채우세요.",
        ["binary_search"],
        2,
        "int search(int* nums, int n, int target) {\n    int left = 0, right = n - 1;\n    while ({{b1}}) {\n        int mid = left + (right - left) / 2;\n        if (nums[mid] == target) return mid;\n        if (nums[mid] < target) left = mid + 1;\n        else right = mid - 1;\n    }\n    return -1;\n}",
        [slot("b1", ["left <= right"], ["left <= right", "left < right", "mid <= right", "left != right"])],
        "구간은 left <= right로 유지합니다.",
        language="c",
    ),
    blank(
        "blank_c_arr_001",
        "C에서 배열을 **순회**하며 최댓값을 구합니다. 빈칸을 채우세요.",
        ["array"],
        1,
        "int array_max(int* nums, int n) {\n    int best = nums[0];\n    for (int i = 1; i < {{b1}}; i++) {\n        if (nums[i] > best) best = nums[i];\n    }\n    return best;\n}",
        [slot("b1", ["n"], ["n", "n - 1", "0", "best"])],
        "인덱스는 1부터 n-1까지(또는 i < n)입니다.",
        language="c",
    ),
    blank(
        "blank_go_bs_001",
        "Go **이분 탐색**입니다. 빈칸을 채우세요.",
        ["binary_search"],
        2,
        "func search(nums []int, target int) int {\n    left, right := 0, len(nums)-1\n    for {{b1}} {\n        mid := left + (right-left)/2\n        if nums[mid] == target {\n            return mid\n        }\n        if nums[mid] < target {\n            left = mid + 1\n        } else {\n            right = mid - 1\n        }\n    }\n    return -1\n}",
        [slot("b1", ["left <= right"], ["left <= right", "left < right", "mid <= right", "left != right"])],
        "Go에서도 left <= right가 기본 루프 조건입니다.",
        language="go",
    ),
    blank(
        "blank_go_slice_001",
        "Go **슬라이스**에 원소를 append합니다. 빈칸을 채우세요.",
        ["array"],
        1,
        "func appendEvens(nums []int) []int {\n    out := []int{}\n    for _, x := range nums {\n        if x%2 == 0 {\n            out = {{b1}}\n        }\n    }\n    return out\n}",
        [slot("b1", ["append(out, x)"], ["append(out, x)", "append(nums, x)", "out = x", "len(out)"])],
        "Go에서는 append(out, x)로 확장합니다.",
        language="go",
    ),
]


def validate_pick(q: dict) -> None:
    assert ID_PATTERN.match(q["id"])
    cids = {c["id"] for c in q["choices"]}
    assert q["correctChoiceId"] in cids
    assert 3 <= len(q["choices"]) <= 4


def validate_blank(q: dict) -> None:
    assert ID_PATTERN.match(q["id"])
    placeholders = set(re.findall(r"\{\{(\w+)\}\}", q["codeTemplate"]))
    blank_ids = {b["id"] for b in q["blanks"]}
    assert placeholders == blank_ids
    for b in q["blanks"]:
        for ans in b["correctAnswers"]:
            assert ans in b["choices"]


def merge_bundle(path: Path, new_items: list[dict], kind: str) -> int:
    data = json.loads(path.read_text(encoding="utf-8"))
    existing = {q["id"]: q for q in data["questions"]}
    for q in new_items:
        if kind == "pick":
            validate_pick(q)
        else:
            validate_blank(q)
        if q["id"] in existing:
            raise SystemExit(f"duplicate id {q['id']}")
        existing[q["id"]] = q
    data["questions"] = list(existing.values())
    data["updatedAt"] = "2026-05-19"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return len(data["questions"])


def sync_files() -> None:
    for d in SYNC_DIRS:
        d.mkdir(parents=True, exist_ok=True)
        shutil.copy2(PICK_PATH, d / "pick.json")
        shutil.copy2(BLANK_PATH, d / "blank.json")
        print(f"synced -> {d}")


def print_stats() -> None:
    from collections import Counter

    for name, path in [("pick", PICK_PATH), ("blank", BLANK_PATH)]:
        data = json.loads(path.read_text(encoding="utf-8"))
        langs = Counter(q.get("language", "python") for q in data["questions"])
        print(f"{name}: {len(data['questions'])} total — {dict(langs)}")


def main() -> None:
    pick_n = merge_bundle(PICK_PATH, EXTRA_PICKS, "pick")
    blank_n = merge_bundle(BLANK_PATH, MULTI_LANG_BLANKS, "blank")
    print(f"pick.json: {pick_n} questions")
    print(f"blank.json: {blank_n} questions")
    sync_files()
    print_stats()


if __name__ == "__main__":
    main()
