### 変更履歴

🌍 [フランス語](CHANGELOG.md) | [英語](CHANGELOG-en.md) | [スペイン語](CHANGELOG-es.md) | [中国語](CHANGELOG-zh.md) | [ドイツ語](CHANGELOG-de.md) | [日本語](CHANGELOG-ja.md) | [韓国語](CHANGELOG-ko.md) | [アラビア語](CHANGELOG-ar.md) | [ヒンディー語](CHANGELOG-hi.md) | [イタリア語](CHANGELOG-it.md) | [オランダ語](CHANGELOG-nl.md) | [ポーランド語](CHANGELOG-pl.md) | [ポルトガル語](CHANGELOG-pt.md) | [ルーマニア語](CHANGELOG-ro.md) | [スウェーデン語](CHANGELOG-sv.md)

- **1.14.1** Mistral：レート制限超過でファイル全体が失敗しなくなり、既定モデルを実測で確認（2026-09-17）：

  - **HTTP 429が発生するとファイル全体が失われていました。** `mistralai` SDKはOpenAIやAnthropicのSDKとは異なり、既定では再試行を一切行いません。また、Mistralの上限は低く、モデルごとに設定されています。リポジトリアカウントでの実測値は、Large 3が1分あたり15リクエスト、Small 4が1分あたり100,000トークンです。Smallで4件の翻訳を同時実行したキャンペーンでは、84件中5件が失われました。クライアントは今後、429、5xx、接続エラーに対して再試行し、待機時間を2秒から60秒まで段階的に延ばしながら、最長5分間継続します。Mistralの429には待機時間が示されず、上限は1分単位で計算されるためです。APIでの対照検証では、Large 3に20回連続で呼び出し、16回目で33秒待機したものの、20回すべて成功しました。
  - **推論ブロックを含む応答でも翻訳が壊れなくなりました。** Small 4とMedium 3.5は、推論を要求すると推論を行い、その場合、応答は文字列ではなく、`thinking`、続いて`text`のブロック一覧になります。どちらも既定では推論しませんが（実測済み）、プロバイダー側で既定値が変更されると最終的に`AttributeError`になっていました。今後はClaudeと同様に、推論ブロックを除外します。
  - **既定モデルを確認：`mistral-large-latest`と`mistral-small-latest`。** これらより新しい唯一のモデルであるMistral Medium 3.5を、14言語すべてについて、互換性表に使用した情報量の多い技術動向記事とREADMEで比較測定しました。記事では、14言語中9言語で小見出しを失うか、その階層を変更しました。差異のない翻訳はわずか1件で、Large 3は6件、Small 4は8件でした。また、入力料金はLarge 3の3倍、出力料金は5倍です。エイリアスはLarge 3（`mistral-large-2512`）とSmall 4（`mistral-small-2603`）を指します。
  - **`MODEL_TOKEN_LIMITS`をAPIに合わせて更新**：Mistralファミリーは256,000ではなく262,144トークン、`ministral-3b`は131,072トークンとなり、`mistral-medium-2604`を含む日付付き識別子でも「一覧にない」という警告が出なくなりました。16,000文字を上限とするセグメント分割に変更はありません。

- **1.14.0** README冒頭の互換性表と、その根拠となる測定キャンペーン（2026-09-09）：

  - **モデルごとの判定をREADME上部にフランス語で掲載。** 300件を超える翻訳結果が文書の中ほどにあり、3つの表に分かれていたため、読み合わせる必要がありました。新しい表ではモデルごとに1行で結論を示し、とりわけ何が異なるのかを明記します。比率ではなく、「アラビア語と日本語で太字の単語が1つ欠落」のように示します。情報量の多い2つの文書に対し、比較ツールで差異が一切検出されなかったモデルは3つです。`gemini-3.7-flash`、ChatGPTサブスクリプション上の`gpt-5.6-sol`、OpenRouter経由の`z-ai/glm-5.2`です。
  - **176件の翻訳を再測定するキャンペーン。** 元の測定は9月4日のもので、それ以降に大幅に変更されたREADMEを対象としていました。このREADMEでは8モデルを再測定し、ブログの技術動向記事では2モデルを`--news`モードで測定し、公開README 4件（FastAPI、Ollama、tldr-pages、Vue.js）では1モデルを測定しました。記録すべき結果は3つありました。Mistralはアラビア語、ヒンディー語、韓国語で**セクション見出し全体**を失いましたが、パイプラインのどのガードも検出できませんでした。見出しはトークンで置換できず、現在、翻訳中にそれを検査する仕組みはありません。ただし、比較ツールでは事後に検出できます。GrokはREADMEでは問題なく処理できる一方、技術動向記事では5言語で失敗し、最初のセグメントだけでインラインコード4個とURL 3個を失いました。Geminiは公開README 4件に対する56件の翻訳のうち、55件を差異なく出力しました。
  - **構造比較ツールをリポジトリに追加。** READMEでは、この手順をモデル評価の適切な方法として「セクション数、リンク数、個別URL数、コードブロック数を比較してください」と説明していましたが、ツール自体は提供していませんでした。これらの表を生成したのが`scripts/compare_structure.py`です。11件のテストにより、URL、コードブロック、セクション、インラインコード、表の行、引用の欠落を検出できることを証明しています。信頼性を確保するために行った非ラテン文字表記に関する2つの修正も含まれています。全角閉じ括弧が後続するURLを別のURLとして数えなくなり、中国語で短くなった引用を欠落した引用として扱わなくなりました。
  - **公開前後にパッケージを検査。** テストスイートがソース上で実行され、緑のままでも、配布パッケージが壊れている場合があります。たとえば、setuptools設定でモジュールが抜けていたり、エントリーポイントを解決できなかったりする場合です。`scripts/check-package-smoke.sh --wheel`はwheelをビルドし、リポジトリ外の使い捨てvenvにインストールして、パッケージだけが含まれていること、2つの実行形式が応答すること、全モジュールをインポートできることを確認したうえで、実際の文書を翻訳して構造を比較します。`--pypi`はインデックスから同じ処理を行います。実際に公開されたものが、まさにそのバイト列であることを証明できる唯一の検査です。PyPIでは同じバージョンを再公開できません。`--full`ゲートは、モデル呼び出しも費用も発生させずに、そのオフライン部分を実行します。
  - **READMEの7つの記述を修正し、すべて書き換え前に再現。** 「誤ったものがディスクに書き込まれることはありません」という記述は誤りでした。モデルがセクションを削除したり、front matterの日付を変更したりしても、パイプラインは`success`ステータスでファイルを書き込みます。これは模擬応答で再現しました。READMEでは今後、トークンが保護するもの（コードブロック、インラインコード、URL、アンカー、引用）と、現在パイプラインのガードが検査しないものを説明します。「差異なし」は「同一」を意味しません。比較ツールは要素の内容を読まず、数だけを数えます。また、レベル4見出しの削除、インラインコードのテキスト置換、旗の入れ替えは報告しません。いずれも実測された事例であり、比較ツールには旗のカウンターがないため、「同じ旗」という記述は削除しました。コントリビューション用のインストール手順では、使用可能なツールを作成できませんでした。`pip install -r requirements.txt`は依存関係だけをインストールし、`python -m aipmt`は`No module named aipmt`と応答し、`pip install -e .`がありませんでした。また、両方の依存関係ファイルに存在しない`pre-commit`のインストール行もありませんでした。小さなコンテキストに関するOpenRouterの説明は、コードと逆の内容でした。コンテキストウィンドウが**16,400トークン**未満のモデルは、呼び出し前に拒否されます。4,095、8,192、16,384で測定しました。プロジェクトの`.env`によってAPI呼び出し先が変更されるのを防ぐフィルターは、どこにも文書化されていませんでした。現在は、対象となる変数の一覧とともに文書化されています。最後に2つの数値を修正しました。冒頭表のGrokのセルは列見出しでは9月4日のキャンペーンとされていましたが、実際には9月9日のキャンペーンに由来していました。また、Geminiについて「リンクを1つ解除」としていた記述は実測結果と逆でした。Geminiは3つの裸URLをリンクに変換しており、URLを1つも失っていません。

  - **書き込み失敗時に切り詰められた翻訳がディスクに残らなくなりました。** `open(cible, "w")`は、ファイルを埋める前に切り詰めます。そのため、書き込み中のエラー（ディスク容量不足など）により、不完全なターゲットが残っていました。再現結果では、8バイトを書き込んで`failure`ステータスを返し、その後の再実行ではこのファイルを検出し、`skipped`と応答して保持していました。つまり、一度の失敗によって切り詰められた翻訳が生成され、それ以降は何も警告せず、終了コードも0になっていました。今後は、同じディレクトリ内の一時ファイルに内容を書き込みます。`os.replace`がアトミックになるのは同じファイルシステム内だけだからです。その後に名前を変更し、割り込みを含め、書き込みが失敗した場合は一時ファイルを削除します。この一時ファイルは`mkstemp`で作成します。レビューにより、予測可能な名前では問題が移るだけであることが判明しました。`cible.md.aipmt-tmp`に配置されたシンボリックリンクによって、翻訳が出力ディレクトリ外のリンク先ファイルへ書き込まれ、`success`が返されました。また、同じターゲットに対する2つの同時実行が同じ名前を共有し、1つ目が同じinodeへまだ書き込んでいる途中で2つ目が名前を変更していました。ターゲットは成功と報告されましたが、内容は混在していました（実測では`BBBBBBBB`ではなく`BBBAAAAA`）。`mkstemp`は`O_CREAT | O_EXCL`で一意の名前を使用して作成するため、この2つの問題を解消します。置換前に既存ターゲットの権限を明示的に引き継ぎます。`mkstemp`は0600で作成されるため、そうしなければ意図的に0600に設定されたターゲットが0664になり、Webサーバーが提供していた0644のターゲットは読み取れなくなっていました。8件のテストで全体を固定し、コードに2つのミューテーションを加えるとテストが失敗することも確認しました。

  - **純粋性マニフェストで、書き換えられた抑制マーカーを宣言できるようになりました。** 検査では、参照側の`# nosec`、`# nosemgrep`、`NOSONAR`を含む各行が、一語も変わらず残ることを要求していました。しかし、書き込みを一時ファイルへ移すと、開かれる変数の名前が変わります。Sonarの抑制は同じでも、その行は変化します。マニフェストの`markers`カテゴリでは、その理由とともに、`old` → `new`の組み合わせを宣言します。条件は2つあり、2つ目はレビューから追加されました。置換後の行が存在し、**元の行と同じ抑制を持っていなければなりません**。この条件がなければ、`value = 1  # NOSONAR` → `value = 1`と宣言するだけで検査に合格し、宣言だけでマーカーを削除できてしまいました。これは、この検査がまさに防ごうとしていることです。宣言されていない消失は引き続き拒否されます。

  - **モデル以外の原因で中断された2つのキャンペーンを表から削除。** GrokはこのREADMEの12言語を処理した後にCLIセッションを失いました。2言語はモデルを呼び出すことなく4秒で拒否されました。また、`qwen3.8-flash`は2言語の処理後、上流ホスティング事業者からHTTP 429による制限を受けました。中断されたキャンペーンは評価対象にできません。最初から最後までやり直すか、まったく行わないかのどちらかです。あわせて、「このプロジェクトのREADME」表の所要時間を9月9日のキャンペーンに合わせて修正しました。以前の値は、測定対象の785行ではなく508行のリビジョンに基づいており、`gpt-5.6-sol`について実測値が6分46秒であるにもかかわらず、2分04秒と記載していました。

  - **READMEを再構成：1,007行から600行へ削減し、読者が読む順番に整理。** ツールの機能、インストール、設定、はじめの一歩、次に互換性表（何を実行するのか理解した後になるよう、インストール後に配置）、オプション、プロバイダーごとの章、詳細な測定結果、最後にコントリビューション方法という構成です。キャンペーンの経緯、測定時の逸話、セクション間の重複を削除しました。残した数値はすべて表の数値と一致し、動作に関する各記述はこのバージョンのコードに対応しています。再構成の記録はgit履歴に残っています。

  - **冒頭の表で、各差異が何言語に該当するかを明示。** 以前は「✅ 14言語」と記載し、その隣の列に「太字の単語が1つ」と記載していましたが、それが1言語だけに該当するのか、14言語すべてに該当するのかを示していませんでした。読者には判断できず、実際の測定結果が良好であるにもかかわらず、悪い印象を与えていました。このREADMEでは、太字の単語が1つ余分なのはGeminiが14言語中1言語、Solが2言語、GLMが3言語だけです。現在は各セルに、影響を受ける言語数と言語名を記載しています。判定列の数値についても、「14言語のうち、翻訳が書き込まれ、何も異ならなかった言語の数」と一文で定義し、3つの記号の意味を凡例で説明しています。分類は所有者によるものです。✅ 差異なし、⚠️ すべて翻訳され、変更はマークアップのみで欠落なし、❌ 少なくとも1言語が拒否されたか、書き込まれたファイルで内容が欠落。

  - **記事のキャンペーン全体を現在の比較ツールで再計算。** 2つの数値は、非ラテン文字表記に関する比較ツールの修正前に公開されており、存在しない差異を数えていました。`qwen3.8-flash`は差異なしが13言語から14言語に、`qwen3.7-flash`は7言語から8言語になりました。`gpt-oss`に関する記述も同時に修正しました。フランス語のまま残された箇所が、配布ファイルに到達したことはありません。未翻訳箇所のガードが、影響を受けた4言語を拒否していました。これは、停止できたモデルと、問題を見過ごして通したモデルの違いであり、READMEで明示しています。

  - **README末尾に免責事項を追加。** GPL v3の第15節と第16節ですでに一切の保証を否認していますが、ツールをインストールする前にライセンスを読む人はいません。そのため、4点を明記しました。自動翻訳は公開前に見直す必要があり、ガードは見出し、表、front matter、意味を対象としていないこと。翻訳対象の文書は、選択したプロバイダーへ、そのプロバイダーの条件に基づいて送信され、一部の無料モデルはやり取りを再利用する場合があること。データを外部へ送信しない唯一の方法はローカルモデルであること。API呼び出しは課金対象であり、プログラムは支出額に上限を設けないこと。そして、公開されている測定値は特定時点での観測結果であり、保証ではないことです。

  - **`gpt-5.6-*`ファミリー全体をChatGPTサブスクリプションから利用可能**であることを実測しました。`--model gpt-5.6-terra`では、APIが既定で提供するモデルをCodex経由で利用できます。既定は引き続き`gpt-5.6-sol`です。情報量の多い文書について、14言語すべてで欠落がないことが実測された唯一のモデルであり、このリポジトリの翻訳にも使用されています。

- **1.13.1** 依存関係の鮮度：遅れを、読み飛ばされる可能性のある警告だけで済ませない（2026-09-09）：

  - **数えられない警告は見落とされる警告です。** `check-deps-fresh.sh`は数日前から`openai`と`anthropic`の更新が遅れていることを示していましたが、ゲートの要約行は失敗数しか数えていませんでした。そのため、数行上に遅れが記載されているにもかかわらず、「準備完了：N件の検査が成功」と表示されていました。最後の行だけを読む人には、つまり誰にでも、その事実が分かりませんでした。今後、判定には警告数も表示され、処理途中でその都度出力する代わりに、専用カウンターで集計します。
  - **遅れとともにリリースノートも表示。** バージョン番号だけでは何が変わったのか分かりません。また、適切なファイルを自分で探す手間こそが、この手順を飛ばす原因になります。この検査では、メジャー更新とマイナー更新の両方について、更新が遅れている各パッケージのCHANGELOGのアドレスを理由とともに表示します。SDKのマイナー更新でも、このプロジェクトが依存する部分が変更されたことがあるためです。
  - **`openai` 3.8.0 → 3.10.0、`anthropic` 1.3.0 → 1.4.0。固定前にリリースノートを確認。** OpenAI側でこの範囲にあった動作変更は1つだけです。浮動小数点数の範囲を超える数値の`Retry-After`ヘッダーがあった場合、短いバックオフへフォールバックせず、再試行なしで元のエラーを返すようになりました。このプロジェクトが依存する部分には変更がありません。モデルが追加フィールドを許容する動作は変更されていないことを、両方のタグのコードで確認しました。そのため、OpenRouterが選択肢に追加する`native_finish_reason`と`error`は引き続き通ります。Anthropic側では、新しいガードにより、SDKが`httpx2`を要求する箇所に`httpx`パッケージのオブジェクトが渡されると、明示的な`TypeError`で拒否されます。このプロジェクトは浮動小数点数しか渡さないことを確認しました。10分を超える非ストリーミング呼び出しを拒否する規則は、2つのバージョン間でバイト単位で同一です。免除されるのは明示的な`timeout`によるものであり、その32,768トークンは21,333のしきい値を超えています。
  - **検証済み**：更新後のバージョンで502件と31件のテストスイートを実行し、`requirements.txt`の閉包がインストール済み環境（41件の固定）と一致することを確認しました。また、各SDK（OpenAIとClaude）から`--news`モードの文書に対して実際に1回ずつ呼び出し、構造がソースと同一であることを確認しました。
- **1.13.0** Provider `--use_openrouter`：約430モデルへの有料ルーター。中国のオープンモデルを含む（2026-09-05）：

  - **8番目と同時に提供される、9番目のProvider経路。** 1.12.0はPyPIで公開されなかったため、OpenCodeとOpenRouterという2つのルーターが同時にリリースされる。[OpenRouter](https://openrouter.ai)では、ここではほかのどのProviderも公開していないモデル（Kimi、Qwen、DeepSeek、Z.ai）へ、従量課金される単一クレジットと1つのキーでアクセスできる。endpointはOpenAI互換なので、clientはxAIと同じである。**このProviderをほかと区別するものはすべてpreflightに集約されており、その各ルールはAPIでの測定結果に基づいている。**

  - **同じモデルが上限の異なる数十のホスティング事業者から提供される一方、ルーティングはその違いを認識しない。** 測定結果：`z-ai/glm-5.2`には33事業者、`z-ai/glm-5.3-flash`には23事業者があり、そのうち1事業者の**出力上限は2,048 tokens**だった。そのため、23事業者を利用する長文翻訳は、何の通知もなくランダムに途中で切れていた。preflightは`/api/v1/models/{modèle}/endpoints`を読み、出力上限が8,000 tokens未満の事業者、ステータスが低下している事業者、上限を申告していない事業者を除外して、残りを固定する。`allow_fallbacks: false`を伴わない`provider.only`は単なる優先指定にすぎず、ルーターは除外済みの事業者へ戻るため、固定は無意味になる。上限を満たす事業者がなければ、コマンドは停止する。それでも翻訳を続けることは、このpreflightが防ぐために存在する無言の切り捨てを受け入れることになる。

  - **推論は出力と同じ料金で課金され、多くのモデルでデフォルトで有効になっている。** `z-ai/glm-5.2`に同じリクエストを送り、「OK」と応答させた結果、**モデルのデフォルトではcompletionが107 tokens、推論を無効にすると2 tokens**だった。推論が何の価値ももたらさない翻訳では、各ファイルの各segmentに18倍の差が生じる。そのため、デフォルトでは無効にしている。推論を必須とする**431モデル中288モデル**（`reasoning.mandatory`）は`400 « Reasoning is mandatory for this endpoint and cannot be disabled »`を返す。それらについては、preflightが受け付けられるeffortを読み取り、最小値を要求する（次項）。effortは、推論が最初に消費する**`max_tokens`の一定割合**を割り当てるため、値を無作為に選ぶと、白紙出力のリスクを減らすのではなく移動させるだけになる。

  - **推論を必須とするモデルには、そのモデルが受け付ける最小のeffortを指定する。この判断も測定に基づく。** 当初はモデルの代わりに推測しないよう、何も送らない方針だった。catalogue上のデフォルトが`max`である`z-ai/glm-5.3-flash`で検証したところ、この方針では翻訳が完了する前に出力が**32,768 tokensで切り捨てられ**、14言語中2言語が失われた。envelopeを増やしても結果は変わらない。effortがその一定割合を割り当てるため、envelopeとともに推論量も増えるからである。そこでProviderはpreflightで`supported_efforts`を読み取り、最小値を要求する。catalogueに利用可能な値が示されていない場合は「何も指定しない」状態へフォールバックする。問題が発生した言語で反証したところ、以前はbudget枯渇で失敗していたが、現在は9分で完了し、構造も原文と同一になった。

  - **上流ホスティング事業者の障害には、今ではその名前が明記される。** ルーターはこのケースを、`native_finish_reason`がnullの`finish_reason=error`として正規化する。2言語で2回測定したところ、いずれも正確に750秒だった。従来の汎用メッセージでは文書や分割方法の不具合を探すよう誘導していたが、現在は障害が供給側にあり、再試行だけで解決することが多いと伝える。

  - **出力が空の`finish_reason=length`は切り捨てではない。** 最初の有用な文字が生成される前に、推論がbudgetを使い切った状態である。測定では、有用な出力148 tokensに対して推論が15,850 tokensだった。この2つのケースでは必要な対処が正反対であり、前者ではsegmentを小さくしても意味がない。メッセージは両者を明示的に区別する。さらに、測定に基づく2つのguardを追加した。上流ホスティング事業者が失敗すると、ルーターが**エラーだけを格納したbodyとともに200を返す**場合があり（`choices[0]`はメッセージを覆い隠す不透明な`TypeError`を発生させていた）、またcontext windowはcatalogueから読み取って`MODEL_TOKEN_LIMITS`に設定する。`DEFAULT_TOKEN_LIMIT`はcatalogue内の44モデルで誤っており、そのうち2モデルの上限は4,095 tokensである。

  - **`--model fournisseur/modèle`は必須であり、ネットワークへ接続する前に形式が検証される。** OpenRouterは単なる供給者ではない。選択には価格、ライセンス、データ処理が関係するため、ユーザーの代わりに決めることはできない。slugはpreflightのURLへ埋め込まれるので、検証は単なる操作性上の配慮ではなく、pathの注入を防ぐguardである。2つのルーターで共有されるnamespace対応regexは`a/b/..`を受け入れるため、親segmentは明示的に拒否される。`--eco`は効果がなく、その旨も表示される。

  - **3つの表現を修正し、そのうち1つは事実誤認だった。** `codex exec`に関するOpenAIの注意事項は、共有runnerへ個人のsessionファイルを注入することを対象としており、repositoryが公開されていることを対象としてはいなかった。README、CLAUDE.md、codeでは意味を取り違えて引用されていた。OpenCodeの認証情報の保存場所は1.18.27で変更され、`auth.json`ではなく`opencode.db`の`credential` tableになった。「ここでは一切読み取らない」というinvariantは引き続き正しいが、所在地の記述が古くなっていた。最後に、OpenCodeのsectionでは、未検証の経路を同等のものとして紹介しなくなった。Zen gatewayとOllamaはend-to-endで測定済みだが、GitHub Copilot、LM Studio、llama.cppは未測定であり、READMEにも現在はそのように記載されている。

  - **測定キャンペーンと、README内の推奨モデル表。** 3種類の文書セットを14言語へ翻訳し、300件を超える翻訳を実行した。対象は、`--news` modeの情報密度が高いブログ記事、このREADMEの標準Markdown、GitHubからそのまま取得した著名プロジェクト4件のREADMEである。この表では、それまで混同されていた2つの項目を区別している。翻訳が**完了したか**、そして**構造が原文と同一か**である。2つの高密度文書で一度も情報を失わなかったモデルは3つある。`gemini-3.7-flash`、ChatGPT subscription経由の`gpt-5.6-sol`、OpenRouter経由の`z-ai/glm-5.2`であり、唯一の差異は、1言語または2言語で`**`の対が保持されなかったことだった。中心的な結論は、**違いを生む要因は`--news` modeではなく文書の密度である**ということだ。subscription経由のGrokはブログ記事では14回中13回失敗した一方、公開READMEでは16回中14回成功しており、原因は長いsegmentでの脱落であることが反証により確認された。この表自体にも注意書きがある。網羅的なものではなく、特定時点の結果であり、所要時間は順位を意味しない。適切な方法は、引き続き自身の文書で測定することである。

  - **構造比較機能は、非ラテン文字で2件の偽陽性を発生させていたため、数値を公開する前に修正された。** 全角括弧`）`が続くURLは、`)`で停止するregexでは正しく分割されず、URL自体は同一でも抽出された文字列が異なっていた。また、フランス語では5行だった引用が中国語では3行に収まり、行単位の集計結果を低下させていた。2つの修正はいずれも反証で検証され、URL、section、inline codeを削除した場合は引き続き検出される。修正しなければ、GeminiとCodexの結果は14言語中それぞれ13言語と12言語ではなく、いずれも11言語として公開されていた。

  - **テスト**：新しいファイル`tests/test_openrouter_provider.py`（76 tests）— modelの検証と親segmentの拒否、ホスティング事業者の固定（上限、ステータス、未申告の上限、共通の最小値）、常にfalseとなる`allow_fallbacks`、`mandatory`に応じた推論の無効化または維持、完全な出力contract（200内のエラー、choiceなし、白紙出力と切り捨ての区別、異常な`finish_reason`、null content）、catalogueへ接続できない場合、slugがない場合、健全なホスティング事業者がない場合にfail-closedとなるpreflight、flagの排他性、ファイル名label。suite全体で**502 tests**。

  - **Refactor：4,253行の単一moduleを、動作を1行も変更せず複数のmoduleへ分割。** `src/aipmt/translate.py`を`config`、`markdown`、`segmentation`、`guards`、`placeholders`、`news`、`prompts`、`notes`、`naming`、`pipeline`、`cli`、およびsubpackage `providers/`へ分割した（Providerごとに1 module、基盤として`base`、解決とdispatchに`registry`）。各移動は個別のcommitであり、その証明は機械的に行われる。検証機能はpackage内の全top-level nodeのASTを基準snapshotと比較し、各symbolの配置、security markerがverbatimで保持されていること、未追跡ファイルがないことを確認する。この一時的なtoolingは次のversionで削除された。外から見える変更点は次のとおりである。`aipmt.translate`はfaçadeとなり、従来moduleが`_` prefixなしで公開していた64個の名前をobject identityを保ったまま再公開する（`__all__`がそのうち9個を保持し、それが正式対応APIである。残りは互換性alias）。また、`import *`が拾っていたdependencyおよびstandard libraryの29個の名前は再exportされなくなった。ファイルの直接実行（`python src/aipmt/translate.py`）は廃止され、`aipmt`と`python -m aipmt`が引き続き対応する2つの形式となる。public functionの`__module__`は、その定義moduleのものになる。SDKは`.env`の読み込み後にimportされるようになり、以前の順序から変わったが、既知の影響はない。427 testsはidentifierまでそのまま保持され、各testが対象とするmoduleへ移された。façade経由だった91個のpatchは、名前を参照するmoduleを直接対象とするようになった（そのうち2つはpatchがなくても成功したことを測定済み）。7つのcontract testがfaçadeを固定する。また、検証をやめたことでgateが成功する事態を防ぐため、gate toolingは最初の移動より前に書き直された。directory単位のLizard scopeと下限、構築済みparserから読み取るflag、package単位のcoverage下限、追跡対象moduleを列挙する`release.sh`である。
  - **修正（pull request review）**：OpenRouterは、`context_length`のないcatalogue recordを拒否するようになった。これまでは128,000 tokensというデフォルト値を測定値として記録し、「modelが一覧にない」という警告まで消していた。また、`finish_reason`がnull（documented typeは`string | null`）の場合はホスティング事業者の生の理由を優先し、`max_tokens`は`length`となる。choice自体にエラーが含まれる場合は、付随するpartial contentを拒否し、正規化された上流障害と同じメッセージを表示する。ホスティング事業者の詳細、生の理由、助言を1つにまとめたものになる。OpenCodeは`part: null` eventに対して`AttributeError`ではなくcontract errorを返し、event lineの1行でも解読できないJSONL streamはpartial textとして受け入れず拒否する。3つのagentic CLIは、呼び出し中にそのprocessが`SIGTERM`を受信するとagentのprocess groupを終了する。regen側の`timeout`ではagentが生存し、quotaを消費し続けていた。また、groupの`SIGKILL`は常にgrace periodに従うため、正常終了するshimがgrandchildを生存させることはない。分割によって離れていた`# fmt: off`と`# fmt: on`の対を再結合した。`--reasoning_effort`のhelpには、これを使用する4つのProviderを明記した。
  - **修正（2回目の再確認）**：OpenRouterへ要求する出力上限は、promptとsegmentが占めるcontext分を確保するようになった。`context_length`は入力とcompletionの両方を対象としており、catalogue内の6モデルでは入力用の余地がないままリクエストが送信されていた。contextが短すぎる場合は、課金前に拒否される。agentic CLIの基盤は、POSIX process groupが存在しない環境では`terminate`、続いて`kill`へフォールバックする。以前のように`AttributeError`がtimeout guardをすり抜け、待機が長引くことはない。OpenCodeの`429` markerはsubstringとしてではなく数値として検索されるようになった。以前は`err_84290b`のようなerror identifierでも90秒のback-offが発生し、その後に結局失敗していた。最後に、canonicalでないOpenRouter endpointはpreflightで表示される。projectの`.env`だけで設定でき、その後、本物のkeyが実際に送信される先だからである。
  - **セキュリティ：projectの`.env`からAPI callをredirectできないようにした。** `find_dotenv(usecwd=True)`はcurrent directoryとその親からファイルを検索する。そのため、信頼できないdirectory tree（cloneしたばかりのrepositoryなど）に、keyを一切知らなくても`OPENROUTER_BASE_URL`、`XAI_BASE_URL`、`OPENAI_BASE_URL`（最後のものはSDK自体が読み取る）を配置できた。その後、environmentまたはuser configurationから得た本物のkeyが、第三者serverのauthorization headerへ送信されていた。filterは一覧ではなくパターンに基づく。インストール済みSDKを調べると12個のrouting variableが読み取られており、そのうちAnthropic clientだけで6個を使用していた。手書きの列挙では半数を見落としていたはずである。そのため、project layerでは、`_BASE_URL`、`_API_BASE`、`_ENDPOINT`に該当するすべてのvariable、proxy、certificate store（管理下のcertificate authorityを指定すると、interceptorを本物のserverと区別できなくなる）、さらに`XDG_CONFIG_HOME`と`APPDATA`を拒否する。これらを設定すると、どのファイルをuser layerとみなすかを決定でき、filterを迂回できるためである。これらのvariableを受け付けるのは、ユーザーが管理する2つのlayer、すなわちexportされたenvironmentと`~/.config/aipmt/.env`だけである。さらにproject layerはinterpolationなしで読み込まれる。`load_dotenv`はデフォルトで`${VAR}`を展開するため、信頼できない`.env`に`NOM_ANODIN=${OPENAI_API_KEY}`が含まれていると、本物のkeyがsubprocessのpattern filterで認識されない名前へ複製されていた。その結果、明示されているinvariantに反して`codex exec`のenvironmentへ入り込んでいた。拒否時にはvariable名だけを表示するようにもした。`https://${CLE}@hôte/`形式のURLでは、拒否しているにもかかわらず、interpolationされたkeyがlogへ漏れていたためである。拒否はstderrへ対処方法とともに出力される。企業用relayはuser configurationで宣言する。
  - **修正：OpenRouterの出力envelopeをcallごとに計算するようにした。** `context_length`は入力とcompletionの両方を対象とするため、ラテン文字のtextを基準に調整した固定reserveでは何も保証できない。`o200k_base` tokenizerで測定すると、16,000文字はフランス語では3,200 tokensだが、日本語では12,300 tokens、絵文字では17,500 tokensになる。そのためbudgetは実際に送信されるtextから算出し、そのUTF-8 byte数で上限を補正する。byteをmergeするあらゆるtokenizer（byte-level BPE、byte fallback付きSentencePieceなど、catalogueで使用される各family）では、1 tokenは少なくとも1 byteに相当する。OpenRouterが未知の数十種類のtokenizerへroutingするこの環境では、これが利用可能な唯一の上限補正である。平均ratioはどれも適さなかった。補助平面のideographでは1 token当たり1.33 bytesまで下がり、combining characterでは1.00 byteまで下がる。現在は、入力と出力が構造上必ずwindow内に収まる。選択したモデルに対して密度が高すぎるsegmentは、課金後ではなくcall前に拒否される。

- **1.12.0** Provider `--use_opencode`：オープンソースagentであるOpenCodeから、任意の供給者へ接続—local model、account不要の無料利用、subscription、またはkey（2026-09-04）：
  - **最初の7つとは性質が異なる、8番目のprovider経路。** [OpenCode](https://opencode.ai) (MIT) はモデルproviderではなく、ユーザーがOpenCode自体に設定した接続先への_ルーター_である。接続先には、APIキー、サブスクリプション（GitHub Copilot、ChatGPT、SuperGrok）、**アカウントなし**で無料モデルを提供するOpenCode Zenゲートウェイ、または**ローカル**モデル（Ollama、LM Studio、llama.cpp）がある。スクリプトはCodexやGrokと同様に、非対話モードで`opencode run`を制御し、同じサブプロセス基盤（専用process group、timeout時に`SIGTERM`、続いて`SIGKILL`、stdinは常に閉じ、環境変数を除去）を再利用する。**2件の実際の翻訳**で検証済み。このREADME全体を`opencode/mimo-v2.5-free`経由で英語に翻訳した場合は49秒、1回のpassのみで、ソースファイルと同一の構造（見出し32件、コードブロックの閉じ26件、リンク18件、URL 37件、表37行、inline code 135件）を保持した。また、試験ファイルを`ollama/qwen2.5:7b`経由でローカル翻訳し、キーを一切使用しなかった。

  - **`--model provider/modèle`は必須であり、これは意図的な選択である。** `--model`がなければ、OpenCodeは自身のデフォルトにフォールバックする。新規インストールでは、それは無料の「stealth」モデル`opencode/big-pickle`であり、その対話内容が学習に使用される可能性がある。実測でも、このモデルが応答した。ユーザーに代わって暗黙にこれを選ぶことは、このリポジトリが追跡している不可視の切り替えそのものである。そのため、エラーメッセージにはモデル一覧を表示するコマンド（`opencode models`）と、3つの例（ローカル、無料、サブスクリプション）が示される。`--eco`は効果がなく、その旨も明示する。`--reasoning_effort`は、明示的に要求された場合にのみ、OpenCodeの`--variant`としてそのまま渡される。

  - **想定ではなく、実測された隔離。** inline設定（`OPENCODE_CONFIG_CONTENT`、OpenCodeのマージ順で最後に位置するため、ユーザー設定を置き換えずに優先される）は、すべてのtoolを拒否する（`permission: {"*": "deny"}`）agent `aipmt`を定義する。registryはモデルにtool自体を提示しなくなり、「ファイル一覧を表示して`id`を実行せよ」と指示されても、モデルはtoolを持っていないと応答する。session共有は無効化し、外部pluginは除外（`--pure`）し、`--auto`は決して使用せず、作業ディレクトリは使い捨ての空ディレクトリとする。2つの暗黙的な注入を実測し、遮断した。`OPENCODE_DISABLE_CLAUDE_CODE`がなければ、ユーザーの`~/.claude/CLAUDE.md`が**すべての**promptに入り込む（単純な「こんにちは」に対して、入力は186 tokensではなく515 tokens）。`OPENCODE_DISABLE_PROJECT_CONFIG`がなければ、現在のディレクトリの`AGENTS.md`も注入される。「各回答をBANANAで終える」という指示が翻訳に適用された。なお、globalの`~/.config/opencode/AGENTS.md`は引き続き注入される。これを除外するswitchは存在せず、流用した`XDG_CONFIG_HOME`で回避すると、ユーザーのproviderまで隠れてしまう。小細工をせず、文書化した。

  - **`exit 0`は何の証明にもならない。3つ目のCLIでも同じ用心が必要であり、これには固有の罠が2つある。** 未知の`--agent`でも`opencode run`は失敗しない。stderrに警告を出し、toolが有効なcoding agentへ**暗黙に**フォールバックする。inline設定が反映されなければ、書き込み可能なagentで翻訳が開始されることになる。そのため、出力contractでは次の条件に加えて、このメッセージが存在しないことも検証する。終了コードが0、`error`イベントがない、`tool_use`がない、最後の`step_finish`が`stop`であること（`length`は切り詰められた応答である）、テキストが空でないこと。2つ目の罠は、errorのJSONイベントが**不透明**であることだ。「予期しないserver errorです。詳細はserver logを確認してください。」という文言と単なる参照しかなく、実際の原因（`ProviderModelNotFoundError: Model not found: foo/bar. Did you mean…`、`ProviderAuthError`など）はlogにしか存在しない。したがって、`--print-logs --log-level ERROR`と、後続するBunのtraceを除いたstderrの`error="…"`フィールドを読み取る。これにより、未知のモデルは原因名を伴って1秒で失敗する。さらに、`--title`は余計なLLM呼び出しを回避する。これがなければ、OpenCodeは`small_model`に対する追加の1 turnでsession titleを生成する。

  - **secret：CodexおよびGrokと同じpatternによるフィルタリングを行うが、明示的に指定された例外が1つある。** `OPENCODE_API_KEY`は保持される。これはOpenCode自体のキー（Zenゲートウェイ、Goサブスクリプション）であり、その名前によってOpenCode宛てであることが明示されている。つまり、OpenCodeの`auth.json`に相当するものであり、aipmtが管理するものでも、課金に使用できるものでもない。providerはOpenCode内（`opencode auth login`、`opencode.json`）で設定し、aipmtの`.env`では決して設定しない。そのため、aipmtのキーがサブプロセスへ到達することはない。サブスクリプションCLIとは異なり、CIでは拒否しない。runner上のAPIキーやself-hostedモデルは正当な用途だからである。

  - **traversal防止guardは、未加工の値ではなく補間後の値を検査するようになった。** `provider/modèle`には、1.10.0のguardが拒否していた`/`が含まれる。`--model`がファイル名`--include_model`へ補間されるため、この拒否自体は正しかった。ファイル名labelは、補間前に`/`、`\`、`:`を`-`へ置換するようになった（`ollama/qwen2.5:7b` → `ollama-qwen2.5-7b`。`:`はWindowsでは不正）。上流のguardは、このlabelを検査する。`../../evil`は出力先配下の単純な名前`doc-en-..-..-evil.md`となり、`..`単体は引き続き拒否され、`--target_lang ../x`も拒否される。`_ensure_within_directory`によるscope guardは、変更なしで第2層として残る。

  - **無料モデルとローカルモデルについて、実測された内容。** `opencode/mimo-v2.5-free`は1段落を16秒、このREADMEを49秒で翻訳する。`opencode/big-pickle`は200語に40秒かかり、同時に2件要求すると、個別には完了する一方で5分間応答がなかった。`opencode/nemotron-3.5-lightning-free`は3分間何も応答しなかった。このため、`REGEN_PROVIDER=opencode`では`REGEN_MODEL`が必須で、並列実行は**2 jobs**とする。ローカル側では、Ollamaがcontextを4,096 tokensに設定することが多い一方、segmentは最大16,000文字に達する。そのため、`PARAMETER num_ctx 32768`を指定した`Modelfile`が必要になる。品質はモデルに依存する。試験ファイルでは、7Bモデルがリストの順序を逆転させ、コードブロックの閉じを壊したのに対し、ゲートウェイのモデルはすべてを保持した。

  - **このリポジトリの翻訳は、今後、課金されるAPIを一切経由しない。** `regen_translations.sh`は、`.env`にキーが残っているだけでOpenAI APIを使用し、Codexはopt-inにすぎなかった。このversionの準備中、まさにそれが発生した。使用量課金を避けるためにChatGPTサブスクリプションが存在するにもかかわらず、28件の翻訳がOpenAI APIへ送られ、その後、ヒンディー語のCHANGELOGがGemini APIへ送られた。キーの自動検出を廃止する。**デフォルトは品質重視モデルの`gpt-5.6-sol`を指定したCodex**とする。`openai`、`gemini`、`grok`には、`REGEN_PROVIDER`に加えて`REGEN_ALLOW_PAID_API=1`が必要であり、判断時点で規則が確実に適用されるよう、例外に明示的な名前を付けた。未知の`REGEN_PROVIDER`はAPIへフォールバックせず失敗する。10件のtestで、デフォルト、拒否、例外を固定する。このversionの28件の翻訳はCodex経由でやり直した。

  - **rate limit時のback-offを共通化した**（`_retry_on_rate_limit`）。CodexとGrokのloopはlabel以外が同一で、3つ目のcopyを追加すると重複thresholdを超えるところだった。3つのCLI errorは共通の`_CliCallError`から派生する。いずれかがその継承関係から外れることをtestで禁止し、共有loopがerrorを見逃さないようにする。

  - **test**：新しいファイル`tests/test_opencode_provider.py`（61 tests）を追加。完全な出力contract、agentのフォールバック、logからの原因取得、重複したtext partの除去とsynthetic partの無視、process groupを終了させるtimeout、429時のback-off、モデルの必須化と検証、secretなしのpreflight、binary解決、dispatchの配線、ファイル名label、traversalの反証を網羅する。`tests/test_review_hardening.py`では、flagの排他性とsecret不在の検証を新しいproviderにも拡張する。gateは、文書化されたargparseの**22 flags**を必須とするようになった。全suiteは**382 tests**。

- **1.11.1** 文書修正：READMEがようやく7つのprovider経路を明記（2026-09-03）：

  - **1.11.0のPyPIページには「4 APIs + Codex CLI」と記載されていた。** 実際のcodeが公開している経路は7つである。API経由のOpenAI、Mistral、Claude、Gemini、Grok、および使用量課金なしでサブスクリプションを使用するCodex（ChatGPT）とGrokである。冒頭文と_Multi-Provider_の項目には2つのGrokモードが欠けており、14件の翻訳も同じ誤りを繰り返していた。packageのlong descriptionはversionごとに固定されるため、掲載内容を修正するには新しいversion番号が必要だった。これがこのversionの唯一の存在理由である。**codeの変更はない。**
  - `CLAUDE.md`を、公開時に導入された内容へ合わせた。gateのcounter（`--full`では16、17）、有効な11件のworkflow、`gh pr checks`では見えない2つのSonar/Codacy counter（hotspots、Codacy API）、`ruff-format`による`# nosemgrep`の移動、OIDC交換に必要なGitHub environment、および_pending publisher_が名前を予約しないという事実を反映した。

- **1.11.0** PyPIへ公開：リポジトリをcloneせず、`pip install ai-powered-markdown-translator`、続いてコマンド`aipmt`を実行（2026-09-03）：

  - **単一ファイルのスクリプトがインストール可能なpackageになった。** `translate.py`をルートから`src/aipmt/translate.py`へ移動し、console entry point `aipmt`と、それに相当する`python -m aipmt`を提供する。貢献するには引き続きリポジトリのcloneが必要である。test、28件の翻訳、品質toolはリポジトリ内に存在する。しかし、利用するだけならcloneは不要になった。

    - **import名は`aipmt`であり、決して`translate`ではない。** 衝突が実在し、しかも暗黙に発生するためである。PyPI package `translate`（v3.8.1、最終upload 2026-07-06）は、同名のディレクトリをインストールする。venv内で再現したところ、ディレクトリがmoduleより優先され、`translate.main`が消え、entry pointは`AttributeError`で壊れる。それでも`pip check`は「壊れたrequirementは見つかりませんでした」と応答し、rc=0となる。ユーザーが単に`pip install translate`を実行するだけで、利用可能な診断情報を出さずにCLIが壊れ得る。実際のwheelによる反証では、そのpackageの上に`pip install translate`を適用し、`aipmt --help`は前後ともrc=0で、両CLIが共存した。
    - **distribution名は長く、コマンドは短い。** `ai-powered-markdown-translator`により、PyPI検索からpackageを見つけられる。acronymだけでは、projectをすでに知っている人以外には見つけられない。公開の目的はまさに、発見可能にすることにある。もっともらしい2つの候補は、検証によって除外した。`ai-markdown-translator`は、同じ目的のtoolによって2024年からnpm上で使用されており、このリポジトリより17か月早い。また、`aimt`は、同じdomainで活動中のpackage `aim`（v3.29.1）と1文字しか違わず、長期的な混同を招く最悪の条件である。方法上の罠もある。`pypi.org/project/<nom>/`はどの名前に対しても200を返すanti-botページであり、信頼できるのはJSON APIだけである。
    - **flat packageではなく`src/` layout。** flat packageならtestの6件の`sys.path.insert(..., "..")`を維持できただろうが、それこそが問題である。これらはpackageではなくsource treeをimportするため、packagingのerrorをすべて隠してしまう。実際のコストは、置換規則を1つ追加することだけである。

  - **キーを一度設定すれば済むようになった。** インストールされたCLIには永続的な設定がなく、環境変数と現在のディレクトリの`.env`しか選択肢がなかった。`find_dotenv`はsystem rootまで上へ探索するため、**ホームディレクトリ配下で作業している場合**には`~/.env`を見つけたが、別の場所で作業すると何も見つからなかった。これは設計上の選択ではなく、コマンドを実行する場所に依存する適用範囲だった。そこで、既存の2層の下に第3層として`~/.config/aipmt/.env`を追加する。

    - **優先順位を明示的にcode化してはいない。** それは`load_dotenv`のデフォルト値である`override=False`から生じる。各layerは、前のlayerで空だった値だけを補う。そのため、環境変数 → projectの`.env` → ユーザー設定という順序になる。この順序は構造ではなく**動作**のtestで検証している。2つの呼び出し順を入れ替えても、第3層を削除しても失敗する。
    - **意図的にTOMLではなく`.env`形式を採用した。** `python-dotenv`はすでにdependencyであり、syntaxは15件のREADMEですでに文書化され、同じファイルを両方のscopeで使用できる。新しいdependencyもsyntaxも増えない。場所は、`XDG_CONFIG_HOME`が**絶対パス**の場合にはそれに従う。仕様では相対値を無視するよう求めており、そうしなければ設定の場所が再び現在のディレクトリに依存してしまう。Windowsでは`APPDATA`に従う。
    - **2つの選択肢を理由付きで除外した。** system keyring（`keyring`）はdesktop環境ではより安全だが、server、container、CIなどのheadless環境では失敗する。これはbatch翻訳そのもののuse caseである。opt-inの候補としては適切だが、デフォルトには適さない。`--api-key` flagでは、キーがshell historyに残り、`ps`にも表示される。
    - **キーがない場合でも、call traceを表示しなくなった。** 以前は、`site-packages`を指すPython stackと、「環境または.env」とだけ述べ、第2の場所をどこに作成すべきか示さないメッセージが表示されていた。現在は、3つの場所すべてを正確なpath付きで列挙し、コマンドはcode 2で終了する。安全網の範囲は**意図的に狭い**。設定phaseだけを`except ValueError`で囲む。実行全体を囲めば、翻訳中に発生した本物のbugが安心感を与えるメッセージへ変換される。このリポジトリが追跡しているfailure modeそのものである。これを防ぐtestでは、`main()`のsourceを読み取る。

  - **修正 — toolをインストールすると、ユーザーの`.env`が無視されていた。** 引数なしの`load_dotenv()`は、現在のディレクトリから上へ探索するのではなく、呼び出し元ファイル、つまり`site-packages`から探索する。独自の`.env`を持つprojectから、実際のconsole entry pointを起動して実測した。`find_dotenv()`は`''`を返し、キーを読み込まないが、`find_dotenv(usecwd=True)`なら見つける。toolがclone済みリポジトリ内でしか動作していなかった間は、このbugは存在しなかった。公開後は常に発生し、正しい設定にもかかわらずAPIキーが「欠けている」ことだけが症状になっていただろう。

  - **3つのgateは、何も検証しなくなった状態でもgreenになっていた。** これらは移動**前**に意図的に強化した。検出対象の変更後に作成したguardでは、何も証明できない。それぞれ元のリポジトリではgreenになり、移行済みcopyではredに変わる。両方向を実測した。

    - **Lizardは存在しないpathを何も言わずに無視する**。rc=0で、「0 file analyzed」となる。complexity gateは、158 functions / 2247 nlocから3 functions / 34 nlocへ変わり、出力は0 byteになっていただろう。scopeは各entryの存在を検証する配列になった。
    - **存在しないmoduleに対する`coverage run --source=`は失敗しない**。stderrへの警告だけで、unittestでも`coverage xml`でもrc=0となり、reportもそのまま公開される。statementsは1453から141へ減り、projectはほとんど分析されていないために健全に見えていただろう。2つの下限でreportをguardする。全体の合計と、計測対象の最大ファイルである。
    - **翻訳の鮮度probeは、呼び出し形式を構造的に認識できない**。argparseのflagをanchorにしているが、ファイル名を変更してもflagは変わらない。再現では、moduleを移動し、15件のREADMEが存在しないコマンドを記載したままでも、「古い翻訳はありません」という判定になった。そのため、第7 sectionではoptionではなく**形式**を検証し、Lizard hookをスクリプトの実際のscopeと照合する。そのkeyである`files:`は、一致しなくなってもpre-commitを失敗させず、hookを**skip**させるためである。
  - **`requires-python = ">=3.10"` はもはや単なる宣言ではありません。** `sonar-project.properties` はすでに 3.10～3.12 を掲げていましたが、開発環境には 3.12 しかなく、一度も実際に検証されていませんでした。公開すれば露呈していた内部矛盾です。現在はテスト workflow が 3.10、3.11、3.12 のそれぞれでスイートを実行し、パッケージをインストールすることで公開されるバージョン境界も検証します。

  - **下限は設定し、上限は設定しません。** `requirements.txt` は引き続きテスト済みの lock であり、`[project.dependencies]` は公開契約になります。lock の厳密なバージョンを公開すると、別のパッケージを利用するすべてのユーザー環境で競合が発生するためです。`<N+1` の上限もありません。設定すれば、メジャーバージョンへの追随遅れがあると release gate を失敗させる `check-deps-fresh.sh` と真っ向から矛盾します。この下限の組み合わせは解決可能であり、反証テスト `openai==1.0.0` は `ResolutionImpossible` で終了します。これは、チェックがすべてを受け入れるのではなく、正しく判別していることを証明します。さらに、`pyproject.toml` のバージョンが CHANGELOG のバージョンと食い違うことを防ぐガードもあります。PyPI では同じバージョン番号を再利用できません。

  - **新しい venv でエンドツーエンド検証済み**：約 70 Ko の wheel に含まれるのは `aipmt/*.py`、dist-info、ライセンスのみです。`aipmt --help` は 22 個のフラグで rc=0、`python -m aipmt` は「usage: \_\_main\_\_.py」ではなく「usage: aipmt」を表示し、`pipx` によるインストールも正常に動作します。そして何より、**任意のユーザーディレクトリから実際に fr→en 翻訳を実行**し、太字、リスト、inline code、リンク、URL が保持され、code block は翻訳されないことを確認しました。移行前から存在する 318 件のテストは、移行前後で識別子リストがバイト単位で完全に同一のまま合格しています。テストが無効化されていないことを証明するのは「OK」ではなく、この事実です。さらに 3 層構成用の 12 件が追加され、合計 330 件です。

- **1.10.0** `--use_codex` Provider（ChatGPT サブスクリプション枠）、SDK とモデルの更新、複数段落にまたがる news 引用の修正（2026-08-29）：

  - **セキュリティレビュー — PR が設けていたものの、すべての箇所では守られていなかった 2 つの安全策**：

    - **Codex の preflight は `.env` 全体をバイナリへ渡していました。** `_codex_preflight` は **`env=` を指定せずに** `subprocess.run` を呼び出していました。そのため、サブプロセスは `os.environ` 全体、つまり `load_dotenv` が読み込んだ `.env` の全内容を継承していました。計測用の偽バイナリで確認したところ、preflight には **7 個の secret**、すなわち 6 provider のキーと `GITHUB_TOKEN` が 1 つ渡っていました。一方、対応する `_grok_preflight` は `env=_grok_env()` を正しく渡しており、secret は **ゼロ**でした。これは PR 内部の不整合です。わずか数行先にある `_strip_secret_env` は、まさにこの不変条件を守るためのものです。`_codex_env_base()` を抽出して両方の経路で共有するようにしました。修正後の計測では、どちらの経路も secret は 0 個です。
    - **「`--deny` は fail-closed」という性質は、実際に使われていた形式には適用されていませんでした。** コメントでは、未知の prefix を持つルールが起動を拒否させるため、Grok の隔離全体が成立すると説明していました。しかし `grok 1.0.13` で計測すると、この検証が存在するのは**括弧付き形式だけ**でした。`--deny 'CeciNestPasUnOutil(*)'` は起動を拒否します（「unknown tool prefix」）が、`--deny 'CeciNestPasUnOutil'` は警告なしに受け入れられます。ところが `GROK_DENY_RULES` は裸の名前だけを使用していました。そのため、xAI 側で tool 名が変更されると、OS sandbox がすでに適用されない環境で、計測済みの唯一の隔離層が何の通知もなく失われる可能性がありました。名前付きの 8 ルールを `Prefix(*)` に変更し、それぞれが CLI の既知の prefix であることを検証しました。catch-all の `*` は、唯一受け入れられるリテラル形式のままです。検証されない形式への後戻りはテストで防止しています。
    - **その他の点も問題がないことを確認済みです**：command injection はありません（常にリスト形式で、`shell=True` は一切使用せず、文書の内容は stdin または `--prompt-file` 経由）。安全でない deserialization もありません（`json.loads` のみを型ガード付きで使用）。path traversal 修正について 7 種類の payload で迂回は見つからず、`--deny '*'` が CLI によって実際に適用されることも確認しました（workdir 外の読み取りで `DENY_ENFORCED` を観測）。
    - 先に追加した鮮度チェックも、自身の原則を迂回していました。PyPI への問い合わせに失敗したパッケージは黙ってスキップされ、gate が成功していました。現在は実際に比較できたパッケージ数を数え、網羅性が不足していれば失敗します。

  - **依存関係を最新化し、遅れの再発を防ぐ 2 つの安全網を追加**：

    - **遅れは実在し、長期間続いていました**：`openai` 2.54 → **3.6.0**、`anthropic` 0.125 → **1.2.0**、`certifi` 2024.8.30 → **2026.7.22**。すべての provider 呼び出しで TLS を検証する root certificate store は 2 年遅れていました。原因も特定済みです。**`.github/dependabot.yml` が存在しませんでした。** このファイルがない場合、GitHub が有効にするのは _security updates_ だけであり、Dependabot が PR を提案するのは CVE の対象となった依存関係だけです。そのため `urllib3` と `idna` は更新された一方で、2 つの SDK はメジャーバージョン 1 世代分も遅れていました。
    - **以前の推論で懸念されていたものとは異なり、2 つのメジャーバージョンは競合せず共存します**。`openai` 3.x と `anthropic` 1.x は **`httpx2`** へ移行し、`mistralai` と `google-genai` は `httpx<1` に残りますが、これらは別々の distribution です。実際のインストールで確認した後、**7 つすべての provider 経路をエンドツーエンドでテスト**しました。対象は OpenAI、Claude、Mistral、Gemini、Grok API、Codex CLI、Grok CLI で、各出力において inline code とリンクが保持されています。「2 つの HTTP stack を避ける」というのは好みにすぎず、阻害要因ではありませんでした。計測によって決着しています。
    - **`requirements.txt` は実際の環境を表していませんでした**。`google-auth`、`cryptography`、`opentelemetry` stack は、宣言されていないにもかかわらず作業用 venv にインストールされていました。そのため、新規インストールではテスト対象の環境を再現できませんでした。反対に、`tokenizers`、`huggingface-hub`、`PyYAML` は、どこからも import も要求もされていないのに記載されていました。`mistralai` 1.x の残骸です。このファイルは、直接依存関係だけから構築した venv の完全な依存閉包として再生成しました。`pip-audit` は、新しい構成に既知の脆弱性を 1 件も報告していません。
    - **`.github/dependabot.yml`**（新規）は、pip と github-actions のバージョンを毎週更新します。minor と patch は 1 件の PR にまとめます。patch 更新ごとに PR を作ると結局無視されるようになり、雑音は更新の敵だからです。**major は個別**とし、それぞれ実際の呼び出しによる検証を必須にします。
    - **`scripts/check-deps-fresh.sh`**（新規、gate に接続）は、遅れをプロジェクトの判定に可視化します。Dependabot は提案するだけで保証はせず、その PR は積み上がる可能性があります。major の遅れは失敗、minor は警告です。常に赤い gate はいずれ無視されるからです。PyPI に接続できない場合は、ローカルでは明示的に skip し、**CI では fail-closed** にします。実行されなかったチェックは成功ではありません。両方向で検証済みです。修正前そのものの状態（`openai 2.54.0→3.6.0`、`certifi 2024.8.30→2026.7.22`）を検出し、minor については警告だけに留めます。

  - **この PR のレビューから得られた修正** — 5 つのレビュー agent が diff を精査しました。以下の項目はすべて修正前に**計測によって再現**されており、そのうち 2 件は同じバージョン内の先行変更によって導入された regression でした。

    - **regression 修正 — `_NEWS_CITATION_REGEX` で指数的 backtracking が発生していました。** 複数段落対応の修正により、繰り返しの中へ `(?:[ \t]*$|[ \t]+.*)` が導入されていました。`[ \t]+` と `.*` の間で空白の分配が曖昧になり、その曖昧さが反復ごとに増幅していました。パターンに一致しない `>   texte` の行、つまり完全に正当な Markdown indentation で計測すると、**14 行で 2,589 ms**かかりました。修正後は 0.04 ms で、行を 1 つ追加するごとに約 9 倍になる状態でした。`--news` mode では、長くて形式に適合しない blockquote が 1 つあるだけで、原因を特定できないまま job timeout まで翻訳が停止していました。現在は反復が行全体を一まとまりとして消費するため（`\n^>(?![ \t]*—).*`）、各反復で一致させる方法は 1 通りしかありません。実際の 231 記事の corpus で検証し、capture の差異は**ゼロ**、引用は同じ 423 件で、複数段落の 14 本の本文も引き続き拡張されています。
    - **2 つの provider flag を同時に指定すると、警告なしに従量課金されていました。** `--use_codex --use_mistral` は受け入れられていました。`_select_provider_client` は Mistral を最初に検査し、`_resolve_provider` は明示的な boolean を優先するため、どちらも Mistral に収束していました。つまりユーザーはサブスクリプション枠を要求したのに、何の警告もなく従量課金を受けていました。これは、まさに `--use_codex` が防ぐために存在する障害形態です。現在は 6 つの provider flag が `add_mutually_exclusive_group` を通ります。**動作変更**：これまで黙って受け入れられていた、2 つの provider を組み合わせた command line は、今後 `argument --use_mistral: not allowed with argument --use_codex` で失敗します。
    - **作業終了時の gate は、probe が異常終了しても成功していました。** `scripts/check-release-ready.sh` にある 13 個のチェックのうち 4 個は、終了コードを一度も確認せず、「stdout を捕捉し、空なら結論を出す」というパターンに従っていました。例外（ファイル名変更、`FileNotFoundError`）は stderr に出力し、stdout を空のままにするため、チェックは「問題なし」と結論づけていました。「`exit 0` だけでは何も証明できない」という罠が、それを防ぐために書かれたスクリプト内で再現されていました。現在は helper `probe()` が終了コード 0 **かつ**終端 sentinel を必須にし、probe は目印の集合が空の場合に結論を出しません。空集合に対する assertion は常に真になるためです。実例として、上記の排他的 group を追加したことで provider flag は `*_group` object を経由するようになり、従来の regex `parser\.add_argument\(` では一致しなくなりました。その結果、**21 個中 6 個の flag** が黙って対象外になっていたにもかかわらず、gate は成功していました。
    - **secret scan は 6 provider のうち 4 つを見逃していました。** character class `[A-Za-z0-9]` はハイフンを除外していました。そのため `sk-proj-…`（現在の OpenAI 形式）と `sk-ant-api03-…` は 2 つ目のハイフンで途切れ、`AIza…` は対象外でした。パターンを拡張し、`.secrets.baseline` は scan から除外しました。また、ガード `.env` は index しか見ない `git diff --cached` を照会していました。そのため、最悪のケースである**すでに commit 済み**の `.env` は決して検出されませんでした。現在は `git ls-files` を照会します。
    - **Codex の「token warm-up」は、実際には warm-up になっていませんでした。** 計測すると、`codex login status` は `~/.codex/auth.json` に触れておらず、mtime とサイズは変化しませんでした。help にも「Show login status」と記載されています。それにもかかわらずコメントでは、token を「一度だけ順次」refresh し、1 回限りの rotating token に対する同時 refresh のリスクを無効化すると主張していました。説明されていた保護は存在しませんでした。現在のコメントはコードが実際に行うことを記述しており、本当の対策は引き続き `max_jobs=4` です。さらに、このチェックは以前無視していた `CODEX_BIN` を尊重するようになりました。`PATH` 内に `codex` がない環境では、「未認証」という誤った診断で失敗していました。
    - **`.env` は subshell 内で source されていました。** `detect_provider` が command substitution 内で呼ばれるため、その export は親 shell に伝播しませんでした。`.env` で定義された `GROK_BIN`、`GROK_HOME`、`REGEN_MODEL` は `main()` 内の読み取りから見えないままで、正しい設定にもかかわらず「Grok binary が見つからない」と判定されていました。
    - **同時実行数が公称上限を 50% 超えていました。** README/CHANGELOG の組を起動した後にガードが配置されていたため、`max_jobs=2` の実測ピークは **3** でした。週次 quota が Chat/Imagine/Voice と共有され、計測もできない Grok では、スクリプトが自ら課した上限すら守られていませんでした。また、最終的な件数は表示されるだけで、28 と比較されていませんでした。そのためファイルが欠けていても検出されませんでした。
    - **Grok の出力契約：`stopReason` が存在しない場合は、今後失敗します。** 公表された契約が `end_turn` を必須としていた箇所で、コードは「`end_turn` **または欠落**」を適用していました。field のない payload、または CLI 更新によって field 名が変更された payload は、ガードを警告なしの no-op にしていました。また、`max_turn_requests` は rate limit として分類されなくなりました。これは turn budget の枯渇であり、再試行しても 90 秒待った末に同じ結果になるためです。`quota` も rate limit marker から除外しました。その理由は `_codex_is_rate_limited` の docstring にすでに記載されていましたが、Grok には適用されていませんでした。
    - **Gemini の cascade はモデル単位で memoize されるようになりました。** default model が拒否するにもかかわらず、各 segment で `minimal` から再開していました。そのため通常経路でも segment ごとに 400 の往復が発生し、同じ警告が繰り返し表示されていました。警告は何百回も繰り返されると読まれなくなり、こうして問題を覆い隠すものになります。
    - **その他**：CI での拒否メッセージが Codex 専用にハードコードされており、`--use_grok_cli` のユーザーを `XAI_API_KEY` ではなく `OPENAI_API_KEY` へ誘導していました。`provider.capitalize()` は「Grok_cli」と「Openai」を表示していました。サブプロセス基盤のコメントは「shim」を両方の CLI に一般化していましたが、Grok binary は native ELF です。正しい根拠は「自身のサブプロセスを spawn する agent」であることです。`subprocess` に関する 12 件の SAST finding は、根拠を添えて `# nosec` / `# nosemgrep` として記録しました。`shell=True` を使わないリスト形式によって injection は不可能であり、文書の内容が argv を通ることもありません。
    - **agent 型サブプロセスには、今後一切 secret が渡りません。** 名前を列挙する deny-list が守っていたのは、**課金**に関する不変条件だけでした（Codex には `OPENAI_API_KEY` を渡さず、Grok には `XAI_API_KEY` を渡さない）。計測すると、ほかにも **7 個の secret** が各サブプロセスへ渡っていました。Anthropic、Mistral、Google、Gemini のキー、もう一方の CLI のキー、そして secret ではないものの通信先を変更する `OPENAI_BASE_URL` です。しかし、この 2 つの CLI は**agent**であり、Grok の agent は多くの Linux 環境で適用可能な OS sandbox なしに動作します。現在は名前の列挙ではなく、**名前のパターン**（`API_KEY`、`_TOKEN`、`SECRET`、`PASSWORD`、`CREDENTIALS`）でフィルタリングしています。そのため、このコードが知らない変数をユーザーが `.env` に追加した場合も保護されます。CLI にこれらは一切不要です。認証情報は `~/.codex` と `~/.grok` に保存され、環境変数には置かれません。環境を強化した状態で、両方の provider を介して**実際の翻訳が正常に完了すること**を確認済みです。
    - **テスト**：新しいファイル `tests/test_review_hardening.py`（21 テスト）は、provider flag の排他性、`stopReason` の契約、news regex の線形性、CI の拒否メッセージ、Gemini の memoization、サブプロセス環境に secret が一切存在しないことを固定します。最後の assertion は**汎用的**であり、どのリストにも名前のないキーでも失敗します。一方、既存の除去テストは自身の定数を映すだけであり、自身の loop の故障以外は検出できませんでした。全 test suite は **311 テスト**です。
  - **2つの新しいGrokプロバイダー**：`--use_grok`（xAI API、キーは`XAI_API_KEY`、従量課金）と`--use_grok_cli`（公式Grok Build CLI、Grokサブスクリプションから差し引かれる仕組みで、`--use_codex`と同じ原則）。
    - **APIモード、約40行**：xAIのエンドポイントはOpenAI互換のため、クライアントと`_call_openai`はそのまま再利用され、変更されるのは`base_url`だけです。必要だった適応は1つだけで、すべてに恩恵があります。`finish_reason`は、OpenAIが`stop`を返す箇所でxAIが返す形式である`end_turn`も受け入れるようになりました。モデル：`grok-4.6`（品質重視）と`grok-4.3`（低コスト）。なお、Grokの低コストモデルでもリポジトリ内では最も高価で、100万トークン当たり$1.25/$2.50なのに対し、`mistral-small-latest`は$0.15/$0.60です。このプロバイダーを選ぶ理由はモデルの多様性であり、価格ではありません。
    - **CLIモード**：Codexを踏襲していますが、実環境によって課された相違点が4つあります。プロンプトはファイル経由で渡されます（`--prompt-file`。CLIはstdinを読み取らず、argvに入れたセグメントは`ps`から見えてしまいます）。出力はstdout上の単一JSONオブジェクトです（JSONLでも`-o`ファイルでもありません）。サブスクリプションで利用できるのは`grok-4.6`と`grok-4.5`だけです。また、sandboxは適用できません（後述）。サブプロセスの起動処理は`_codex_run_process`でCodexと共通化されており、テスト済みのCodexプロバイダーの残りの部分には手を加えていません。
    - **`exit 0`では何も証明できないことを実測**：未認証の場合、CLIは**stdout**に`{"type":"error","message":"Not signed in."}`を書き込み、終了コード**0**を返します。拒否やターン数超過も同様に動作します。そのため、出力契約では4つの条件を同時に満たす必要があります。終了コードが0であること、エラーペイロードがないこと、`stopReason == end_turn`、そしてテキストが空でないことです。事前チェックも同じ論理に従います。ログアウト状態でも`grok models`は0で終了するため、stdoutに「not authenticated」が存在する場合にのみ未認証と判断できます。
    - **隔離：非対称性を意図的に採用し、文書化。** Codexが`--sandbox read-only`で動作する一方、最近の多くのLinux環境では、Grokのsandboxは`sudo`なしには回避できない2つの独立したシステム上の理由により適用できません。Ubuntu 24.04以降ではAppArmorが非特権ユーザー名前空間を遮断し（`bwrap: setting up uid map: Permission denied`、Grok以外でも再現）、また`/run/podman`が`0700`の場合、コンテナーランタイムのソケットに対する拒否リストが失敗します（リゾルバーが補足するのは`ErrorKind::NotFound`だけで、EACCESは致命的になります）。最大の落とし穴は、適用できない**組み込み**プロファイルを指定すると、**隔離されない状態で黙って起動する**ことです。そのため、スクリプトは既定ではプロファイルを一切要求せず、黙ってフォールバックすることもありません。代わりにstderrへ警告を出します。保護はCLIの`--deny`ルールに依存し、包括的な`*`も含まれます。実測で確認された唯一の_フェイルクローズ_層であり、未知のプレフィックスを持つルールが1つでもあれば起動を拒否します。`GROK_TRANSLATE_SANDBOX=read-only`でこの隔離を必須にでき、その場合、マシンが要件を満たせなければ起動に失敗します。
    - **安全策**：`XAI_API_KEY`、`GROK_API_KEY`、`GROK_SANDBOX`はサブプロセスの環境から削除されます（キーがあると従量課金へ切り替わり、継承された`GROK_SANDBOX`が適用不能なプロファイルを誤解を招くメッセージとともに強制してしまいます）。MCP・hooks・skills・agentsのスイッチは無効化され、`--disable-web-search`、`--no-subagents`、`--no-plan`、使い捨ての作業ディレクトリ、CIでの拒否、プロセスグループを終了させるタイムアウト、レート制限時のバックオフを採用しています。`--max-turns`は1ではなく6に設定されています。カウンターはツール実行ターンの後に増加するため、1では出力が途中で切れてしまいます。
    - **クォータ**：Grokのプールは週単位で、**Chat、Imagine、Voiceと共有**されます。さらに、これを表示するコマンドはありません。一方、Codexでは`account/rateLimits/read`によって使用量を数値化できます。そのため、`regen_translations.sh`は同時実行数を2に制限し、明示的に警告します。
    - **テスト**：新しいファイル`tests/test_grok_provider.py`（24件のテスト）。テストスイート全体で**290件のテスト**。
  - **修正済みのバグ — 複数段落の英語引用は一部しか保護されていなかった（`--news`モード）**：`_NEWS_CITATION_REGEX`が引用本文として受け入れていたのは、**連続する**`>`行だけでした。引用が複数の段落にまたがると（空の`>`行で区切られる場合）、最後の段落だけが取得されてプレースホルダーに置き換えられ、それ以前の段落はLLMへ送られて翻訳されていました。これは`--news`が保証するために存在する動作とは正反対です。繰り返しは内部の空の`>`行も受け入れるようになり、さらに非貪欲化されました。これにより、最初に現れる空行ではなく、斜体行の直前にある空の`>`で停止します。
    - **実際の規模を測定**：実在する198記事のコーパスでは、419件の引用のうち11件が該当しました。回帰はありません。新しい正規表現が取得する引用数は従来と完全に同じで、複数段落の本文だけが拡張されています（408件の本文は同一、11件は拡張）。また、帰属表示行`> — …`が本文へ取り込まれることは引き続きありません（先読みを維持）。
    - **エンドツーエンドでの実証**：69KBの記事を日本語とアラビア語へ翻訳したところ、以前は引用の最初の段落が日本語で`> GLM-5.3がオープンウェイト化。`となり、アラビア語でも同様に翻訳されていましたが、現在は`> GLM-5.3 is now open-weight.`のまま保持されます。英語引用の行数は9行から10行へ戻り、原文と一致しました。
    - なお、この不具合は後段のバリデーターでは検出されませんでした。バリデーターは引用の存在を確認するだけで、完全に保持されているかまでは確認していないためです。
  - **既定プロバイダーでのコスト削減を実測**：モデル名が`gpt-5`で始まる場合、`_openai_extra_kwargs`は`--eco`でも`reasoning_effort="medium"`を送信していました。`gpt-5.4-mini`で10語の文を翻訳して測定した結果、`medium`では推論トークン45、出力トークン65、`none`ではそれぞれ0と14でした。翻訳に推論は何の利点もなく、すべてのファイルの全セグメントで費用が発生していました。既定値は`--eco`では`none`となり、それ以外では引き続き`medium`です。CLIで明示的に渡された値は、引き続き優先されます。`--reasoning_effort`は`low`・`medium`・`high`に加え、`none`と`xhigh`も受け入れるようになりました（すべてのモデルが全値を受け入れるわけではありません。たとえば`minimal`は`gpt-5.4-mini`に拒否されますが、既存のパラメーターなし再試行がこのケースに対応します）。
  - **SDKの更新とGemini移行**：`google-generativeai`（サポートは2025-11-30に終了し、リポジトリもアーカイブ済み）を統合SDKの**`google-genai`**へ置き換えました。`genai.Client(api_key=...)`の後に`client.models.generate_content(model=, contents=, config=)`を使用し、システムプロンプトはセグメントへ連結せず、`system_instruction`として渡します。`mistralai`は**2.9.4**へ更新されました（importは`from mistralai.client import Mistral`に変更。旧形式は`ImportError`を発生させることをwheelで確認済み）。`anthropic`は**0.125.0**、`openai`は**2.54.0**へ更新しました。これらは`httpx2`への切り替え前の最終バージョンであり、venv内に2つのHTTPスタックを共存させないためです。これに伴い、`httpx` 0.28.1と`pydantic` 2.13.5も解禁されました。
  - **ドキュメントではなく実際のテストで検出された2つの回帰**：
    - `anthropic` ≥ 1.0では、`max_tokens`から10分を超えることが予想される非ストリーミング呼び出しをクライアント側で拒否します（`ValueError: Streaming is required...`）。この安全機構は0.34.2には存在せず、`max_tokens=32768`を使うすべてのClaude呼び出しを壊していました。明示的な`timeout`（`CLAUDE_TIMEOUT`、既定値900秒）で修正しました。これにより、完全な応答だけを利用する呼び出しをストリーミングへ切り替えずに済みます。
    - `thinking_level="minimal"`を受け入れるのはGeminiカタログの一部だけです。`gemini-3.1-flash-lite`は対応していますが、`gemini-3.7-flash`と`gemini-3.1-pro-preview`は400で拒否します。そのため、`_gemini_generate_with_fallback`では`minimal` → `low` → thinking_configなし、という段階的フォールバックを採用しました。既存のOpenAIフォールバックと同じ方式です。最適化用パラメーターのために翻訳全体が失敗してはなりません。
  - **既定モデルを刷新**し、それぞれ実際の呼び出しで検証しました。OpenAIは`gpt-5.5` → **`gpt-5.6-terra`**（28件のバッチで−60%）、`gpt-5.4-mini` → **`gpt-5.6-luna`**（−73%）。Claudeは`claude-sonnet-4-6` → **`claude-sonnet-5`**（より安価で新しい）、`claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**（日付なしの正規ID）。Geminiは`gemini-3.1-pro-preview` → **`gemini-3.7-flash`**、`gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**（安定版で、`3.5-flash-lite`より安価）。Mistralは変更せず、`mistral-large-latest`が4つの中で引き続き最高の費用対効果を示します。なお、`gemini-3.1-pro-preview`より新しいProクラスのGeminiモデルは存在しません。2026年5月に発表されたGemini 3.5 Proは結局リリースされず、3.5/3.6/3.7系列はすべてFlashのみです。
  - **Gemini切り替え前にA/B比較を実測**：`README.md`を`gemini-3.1-pro-preview`と`gemini-3.7-flash`でそれぞれ日本語へ翻訳しました。構造は完全に同一で（リスト21件、コードブロック18件、HTMLリンク13件、画像13件、すべてのURLを保持）、所要時間は**48秒に対して8秒**でした。この2モデルを翻訳または非ラテン文字のスクリプトについて比較した公開ベンチマークは存在しないため、この測定がなければ切り替えは単なる推測に基づくものになるところでした。
  - **Claude応答ブロックのフィルタリング**：`_call_claude`は種類をフィルタリングせずに`block.text for block in response.content`を実行していました。適応型推論モデル（Sonnet 5以降）は`thinking`ブロックを途中に挿入します。このブロックが公開するのは`.thinking`であり、`.text`ではありません。そのため、翻訳は最初のセグメントで不透明な`AttributeError`により失敗する可能性がありました。現在は`thinking`、`redacted_thinking`、`tool_use`、`tool_result`の各ブロックを除外しています（テキストを持つ未知の種類を許容できるよう、否定リストを採用）。テキストブロックが1つもない応答では、明示的なエラーを発生させます。`thinking={"type": "disabled"}`は各呼び出しに渡されます。
  - **`MODEL_TOKEN_LIMITS`を再同期**：廃止日を過ぎたモデルを削除しました（`magistral-*`系列は2026-07-31に廃止、`gemini-2.0-*`は2026-06-01、`gemini-3-pro-preview`は2026-03-09、ならびに`claude-3-5-sonnet-20240620`、`claude-3-7-sonnet-20250219`、`claude-opus-4-1-20250805`、`claude-sonnet-4-20250514`）。上限値を修正しました。Mistralは128K → **256K**（Large 3 / Small 4世代）、Geminiは1 000 000 → **1 048 576**（実際の入力上限）、`claude-opus-4-5`は200K → **1M**、`gpt-5.6-*`系列は400K → **1.05M**。Claude 5（`claude-sonnet-5`、`claude-opus-5`、`claude-fable-5`）、`claude-opus-4-8`、Gemini 3.5/3.6/3.7、`mistral-medium-latest`、`ministral-*`系列を追加しました。なお、これらの上限値は引き続き目安にすぎません。`translate()`がセグメント分割を`min(16000, limite)`に制限しているためです。
  - **Provider `--use_codex`**：従量課金の API を呼び出す代わりに、公式 Codex CLI（`codex exec`）を非対話モードで操作する5番目の provider。翻訳には、すでに支払い済みの ChatGPT サブスクリプション枠が使用される。これは、この用途について OpenAI が文書化している唯一の方法である。プラン別の利用可否マトリクスでは、「Codex SDK、`codex exec`、およびスクリプト化可能なワークフロー」が Plus/Pro/Business/Enterprise で利用可能と記載されている。一方、`~/.codex/auth.json` の token では API Platform への呼び出しを認証できない（また、このスクリプトがそれを読み取ることもない。認証と refresh は引き続き CLI が管理する）。
  - **Codex バイナリを npm だけでなく pip でもインストール可能に**：`_resolve_codex_binary()` は、`CODEX_BIN`、次に `PATH`、続いて OpenAI が公開する公式 Python package **`openai-codex-cli-bin`**（SDK `openai-codex` の依存関係）からバイナリを検索する。したがって、Python プロジェクトで `--use_codex` を使用するために、npm のグローバルインストールは不要になった。この package は `requirements.txt` には追加されていない。バイナリのサイズが約250 MBあり、オプションの provider のために全ユーザーへ強制することになるためである。エンドツーエンドで検証済み：`codex` が `PATH` に存在しない状態でも、解決処理によって同梱バイナリが検出され、完全な翻訳が6秒で完了する。
  - **「サブスクリプションモード」の保証**：`OPENAI_API_KEY` と `CODEX_API_KEY` は subprocess の環境から削除される。この保護がなければ、`.env` に存在するキーによって、目に見える通知なしに Codex が従量課金へ切り替わる可能性がある。この provider は、まさにそれを防ぐために存在する。
  - **テストで固定された CLI の注意点**：
    - `codex exec` は、prompt が引数として渡された場合でも stdin を読み取る。stdin を閉じなければ、コマンドはモデルを一度も呼び出さないまま timeout まで待機する（再現結果：180秒後に exit 124、0 byte）。したがって、`communicate(input=...)` は必須である。
    - npm でインストールされた `codex` は、実際の Rust バイナリを `spawn` する Node shim である。このバイナリは Python process の**孫 process**であり、`subprocess.run(timeout=)` の `SIGKILL` 後も存続して quota を消費し続ける可能性がある。そのため、`Popen(start_new_session=True)` + `os.killpg` が必要となる。
    - CLI は `turn.failed` を出力していても、終了コード0で終了することがある。return code に加えて JSONL 出力（`--json`）も検査し、終了コードが0でも `-o` が存在しない場合は、空の segment を生成する代わりに明示的なエラーを送出する。
  - **rate limit 時の back-off**：CLI には内部 retry が実装されていない（`max_retries = 0`）。分類は部分文字列ではなく JSON payload の構造（`status: 429` / `error.type`）に基づいて行われる。「quota」という語は、回復可能な 429 と恒久的な `insufficient_quota` の両方に現れるためである。
  - **CI 保護**：`CI` または `GITHUB_ACTIONS` が定義されている場合、`--use_codex` は拒否される。サブスクリプションによる認証は共有 runner 向けではなく、OpenAI も公開 repository でこのワークフローを使用しないよう明示的に推奨している。
  - **モデル**：`gpt-5.6-sol`（品質）と `gpt-5.6-luna`（`--eco`）。`gpt-5.6-*` family は CLI と API Platform に共通しているが、ChatGPT account ですべてを利用できるわけではない。allowlist は local validation なしに server side で適用され、一般的でない model を指定すると warning が表示される。Plus plan では、5時間の window あたり Sol が10～100 messages であるのに対し、Luna は250～2,000 messages を提供するため、あらゆる batch processing には `--eco` が推奨モードとなる。
  - **修正済みの bug — 完全に成功しても `regen_translations.sh` がエラー終了していた**：`trap ... EXIT` は、trap の実行時にはすでに存在しない `main()` の `local` variable、`failed_log` を参照していた。`set -u` では、これによって `failed_log: unbound variable` が発生し、28件の翻訳がすべて正しくても script が終了コード1で終了していた。その結果、最もコストの高い再生成直後の段階で `release.sh --auto`（`set -e`）が中断される恐れがあった。variable を global に変更し、trap がその存在を確認するようにした。有益な副作用として、これまでこのエラーに隠されていた実際の翻訳失敗が、終了時の summary に再び表示されるようになった。
  - **`REGEN_MODEL`**：`regen_translations.sh` の新しい environment variable。provider の default よりも優先して特定の model を強制する。たとえば、volume 重視の model `--eco` ではなく、サブスクリプション quota 内の上位 model で再生成する場合は `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol` を指定する。
  - **`regen_translations.sh`**：明示的な opt-in で利用可能な `REGEN_PROVIDER=codex`（ユーザーが気づかないうちにサブスクリプション quota を消費しないよう、自動検出は一切行わない）。並列処理を開始する前に、token を逐次的に1回だけ refresh する。Codex の refresh は rotation 式かつ1回限りであり、job を並行実行すると session `codex login` が無効化されるためである。また、concurrency は4に制限される。
  - **関連 refactor**：`_dispatch_provider_call` は、chain 全体に4つ目の boolean を伝播する代わりに provider 名を返す `_resolve_provider()` を使用し、parameter 数を8から6へ削減した。`Namespace` が最小限しかない状態で `translate(..., use_mistral=True)` を呼び出す test を維持するため、明示的な boolean は引き続き `args` より優先される。
  - **テスト**：新しいファイル `tests/test_codex_provider.py`（48 tests）で、argv、不要情報を除去した environment、前置き禁止 contract、silent failure、timeout/killpg、back-off、preflight、provider resolution、Gemini reasoning cascade、Claude block filtering、および複数段落の news citation を網羅。suite 全体では290 tests。
  - **実環境での検証**：プロジェクトの `README.md` を Codex で**14言語**へ翻訳した結果、reference translation と厳密に同一の構造が得られた（14 code blocks、24 headings、25 table rows、13 HTML links、13 images、19 URLs、code blocks は一文字単位で同一、placeholder の残留ゼロ）。`--news` mode で69 KBの news article を処理した場合、`gpt-5.6-luna` と `gpt-5.6-sol` の出力はいずれも en/ja/ar で downstream の application validator を通過する。`account/rateLimits/read` で測定した消費量は、`--eco` mode で counter の丸め閾値未満（5時間 window の0%）にとどまった。

- **1.9.2** ネストした括弧またはフランス語 prefix を含む news attribution URL の抽出を修正（2026-05-11）：

  - **修正済みの bug**：`_protect_news_quotes` における attribution URL の抽出には、regex `re.search(r"\((.+?)\)", attribution)`（括弧間の lazy capture）が使用されていた。`(relayé par [@user sur X](https://x.com/.../123))` のような attribution（ネストした括弧：外側の `(` + markdown link の `]()`）では、capture が最初に現れた `)` で停止し、文字列が切り詰められたうえにフランス語 prefix まで含まれていた：`relayé par [@user sur X](https://x.com/.../123`（末尾の `)` なし）。その結果、`_validate_news_post` が翻訳済み出力からこの文字列を検索して必ず失敗していた（理由は2つ：`)` が切り詰められていること、および「relayé par」が `relayed by`/`weitergeleitet von`/… に翻訳されること）。low → medium → high → gpt-5.5 の cascade 全体でも通過できなかった。
  - **修正**：regex を `re.search(r"\]\(([^)]+)\)", attribution)` に変更。markdown link の `](url)` を特定して対象とし、**純粋な URL のみ**を capture する（フランス語 prefix も切り詰めも含まない）。この不変性は、翻訳中に placeholder `#URL{N}#` によって保持される。問題となっていた以下の2 pattern に対応：
    - `(relayé par [@account sur X](url))` — ネストした括弧
    - `via [@source](url)` または `selon [@author](url)` — 外側の括弧を伴わないフランス語 prefix
  - **テスト**：`test_silent_failure.py` の class `TestNewsCitationExtraction` に2件追加：
    - `test_extract_attribution_url_with_nested_parens`（Genspark CEO E2B の bug を正確に再現した case）
    - `test_extract_attribution_url_with_french_prefix`（`via` を使用する variant）
  - **coverage の不足**：`check-editorial-coverage.py` は編集上の構文を検証するが、translator による翻訳可能性は検証しない。将来的な改善案（v1.9.2 の scope 外）として、公開**前**にリスクのある pattern を検出するため、dry-run で attribution 抽出を simulation する check が考えられる。

- **1.9.1** 翻訳 note marker 内の CTA label の i18n を修正（2026-05-10）：

  - **修正済みの bug**：翻訳ファイル上部の marker banner にある CTA link の label `[Voir le projet sur GitHub ↗]` が、`target_lang` に従わず、すべての対象言語で**フランス語のまま**になっていた。これは LLM には一切渡されない（URL と repository slug を保持するため Python side で組み立てられる）ため、翻訳 phase では修正できなかった。v1.9 で `marker` format を追加して以来の silent regression。
  - **修正**：15言語を各言語の localized label に対応付ける新しい constant `_VIEW_PROJECT_LABELS` を追加。`_translation_note_invariants(target_lang)` と `_assemble_translation_note_paragraphs(phrase, target_lang)` は、対象言語も伝播するようになった。言語が不明な場合は `fr` へ fallback する（安全策として KeyError を回避）。
  - **テスト**：`test_source_emits_three_paragraphs_repo_title_description_link` を調整（target_lang `ja` → 日本語 label を期待）。2件の新規 test：`test_source_link_label_localized_per_target_lang`（Latin script、表意文字、abjad を含む7言語で parameterize）と `test_source_link_label_falls_back_to_french_for_unknown_target`。合計：`test_translation_note_position.py` で40 tests（従来は38）。
  - **後方互換性**：default `target_lang="fr"` を持つ signature。`args.target_lang` を指定しない外部の programmatic caller も、変更なしで引き続き動作する。
- **1.9** silent-failure 修正 + 完全な品質ツール群 + 複数位置対応の翻訳注記（2026-05-07）：
  - **複数位置対応の翻訳注記 + "embed card" マーカーフォーマット**：
    - 新しい CLI オプション（追加のみ、デフォルトは変更なし → **非破壊的**）：
      - `--note_position {top,bottom,both}`（デフォルト：`bottom`）：翻訳済みファイルの先頭、末尾、または両方に注記を配置。
      - `--note_format {legacy,marker}`（デフォルト：`legacy`）：
        - `legacy` は v1.8 の動作（太字段落 `**…**`）を **byte-for-byte** で厳密に再現。
        - `marker` は、非表示の Markdown link reference definition（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`）に続けて、"GitHub repo embed card" 形式で表示するために構造化された **3段落の blockquote** を出力：inline code のプロジェクトタイトル（`**\`ai-powered-markdown-translator\`\*\*`）、LLM によって翻訳された説明、表示される矢印付き CTA リンク（`[Voir le projet sur GitHub ↗](URL)`）。remark plugin によりビルド時に利用可能（jls42.org のブログ → plugin `remark-translation-banner` を参照）。
    - **LLM に一切送信されない不変要素**：リポジトリタイトルと GitHub URL は、説明文の翻訳後に Python 側で組み立てられる。LLM は slug `ai-powered-markdown-translator` も `https://github.com/jls42/...` も一切認識しないため、renderer／大文字・小文字／scheme が変更されないことを保証。
    - **frontmatter-aware insertion**：`top` または `both` モードでは、注記は YAML frontmatter の終了 **`---` ブロックの後** に挿入（Astro Content Collections／gray-matter の安全性を確保）。helper `_split_frontmatter` はファイル先頭の `---\n…\n---\n` を検出して完全性を維持し、終了 fence のない開いた frontmatter では **`RuntimeError` を送出**（誤った位置に注記を書き込む代わりに、ファイルを `failed_files` に記録）。
    - **ホワイトリスト方式のモデル sanitizer**：`_sanitize_model` は `[A-Za-z0-9._:/-]` に含まれない文字をすべて `_` に置換し、空の場合は `unknown` にフォールバック。Astro の remark plugin 側 validator と整合させ、マーカー形式を破壊する文字（空白、引用符、括弧、カンマなど）を無害化。
    - **内部 refactor**：`_append_translation_note`（1つのモノリシックな関数）→ 7つの純粋 helper（`_translation_note_invariants`、`_build_translation_note_phrase`、`_assemble_translation_note_paragraphs`、`_build_translation_note_source`、`_sanitize_model`、`_quote_lines`、`_split_frontmatter`、`_build_translation_note_block`、`_compose_with_notes`）。builder と composer を分離（builder は区切りなしの純粋なブロックを返し、composer は位置に応じて `\n\n` を適用）；本番処理とソース helper は同一の3段落 assembler を共有。
    - **空行を維持する `_quote_lines`**：各行の先頭に `> ` を付け、空行は `>` のみに変換。これにより mdast は、改行を含む単一段落ではなく、blockquote 内の3つの独立した段落（タイトル／説明／リンク）として認識可能。
    - **適応型 `_build_translation_note_block`**：LLM が維持した段落数に応じて処理（3 = 完全な card 形式、2 = 文 + リンク、1 = fallback）。1段落の fallback では、Markdown リンク `](` が検出された場合、**`**...**` で囲まない**ように変更（リンクの周囲に `<strong>` を配置すると表示が不安定になるため）。
    - **後方互換性**：`_compose_with_notes` 側の `getattr(args, "note_position", "bottom")` と `getattr(args, "note_format", "legacy")` — これらの属性を持たない Namespace（既存テスト、外部からのプログラム呼び出し）も変更なしで引き続き動作。
  - **長文翻訳での silent-failure 修正**：
    - 全 provider（OpenAI、Mistral、Claude、Gemini）で翻訳後の言語を検証：決定論的レイヤー（ソース抜粋がそのまま残っているかを検出）+ 確率的レイヤー（`langdetect`）
    - `finish_reason`／`stop_reason` のホワイトリスト：ホワイトリスト外の状態（truncation、content_filter など）では必ず `RuntimeError` を送出
    - Claude の `max_tokens`：`4096` → `32768`（16k セグメントで潜在的な truncation を回避し、FR→JA/ZH/KO/AR/HI の cross-script 用マージンを確保）
    - heading-aware segmentation：セグメント後半の H2/H3 を優先（各セグメントが意味的に完全なセクションから開始）
    - 非ゼロの exit code までエラーを伝播：`translate_markdown_file` は型付きステータス `success`／`failure`／`skipped` を返し、1つ以上のファイルが失敗した場合は `main()` が `sys.exit(1)`（単一ファイルと batch の両方）
    - 全 provider に empty-content guard、ソース／出力の sanity ratio（500文字以上で 5% 未満なら拒否）、code placeholder の検証（`#CODEBLOCK`／`#INLINECODE`）、LLM 後の正規化（heading に連結された区切り／リンク）、`BadRequestError` では `reasoning_effort` なしで retry
    - 依存関係 `langdetect==1.0.9` を追加
  - **pre-commit 品質ツール群**（「完全な EurekAI 方式」、14 hooks）：
    - Pre-commit：ruff（lint+format）、shellcheck、prettier（md/yaml/json）、detect-secrets（4つの API key を保護）、Lizard（CCN ≤ 12）、pre-commit-hooks v5（whitespace、EOF、large-files、shebangs など）
    - Pre-push：mypy（段階的な lax mode）、Opengrep SAST（translate.py + scripts/）、pip-audit（初期 reporting mode）、unittest discover（tests/ + scripts/tests/）
    - `./venv/bin/python` を使用するローカル wrapper を `scripts/` に配置
    - `scripts/audit_verdict.py`：11件の unittest を備えた pip-audit JSON parser、jls42-astro parser を Python に移植
    - 初期の ruff 違反7件を修正：B904（raise from）×2、B007（未使用の dirs）、C408（dict literal）、C419（list-comp）、SIM105（contextlib.suppress）、SIM110（any()）
    - Lizard は一時的に `translate.py` を除外（CCN 21～47 の関数が4つ、refactor を計画済み）— scripts/ には厳格な gate を適用
  - **SonarCloud + 包括的な coverage**：
    - GitHub Actions workflow `SonarCloud`（sonarcloud.yml + sonar-project.properties）：push および pull-request ごとに分析し、`coverage.xml` で coverage を測定
    - README 上部に SonarCloud badge を11個追加（Quality Gate、Security／Reliability／Maintainability ratings、Coverage、Vulnerabilities、Bugs、Code Smells、Duplicated Lines、Technical Debt、Lines of Code）
    - `tests/test_silent_failure.py`（stdlib の `unittest`）：silent-failure のエラーチェーンを構成する6つの要素を網羅
    - `tests/test_orchestration.py`（+79 tests）：`translate.py` の orchestration layer を網羅（`_resolve_*_filename`、`_existing_translation_exists`、`_record_translation_status`、`_write_output_file`、`translate_directory`、`_validate_input_paths`、`_init_*_client`、`_select_provider_client`、`_normalize_collapsed_markdown`、`_cleanup_source_flag`、`_validate_news_flags_*`、`_openai_create_with_fallback` の TypeError + BadRequestError fallback、o1-series prompt format、`_validate_translation_output` の early-return branch）
    - `scripts/tests/test_audit_verdict.py`：`main()`（stdin/stdout）および `if __name__ == "__main__"` ブロックを subprocess 経由でカバー
    - **新規コードの coverage**：75.5% → 約98%（translate.py 98%、scripts/audit_verdict.py 97%）
  - **テスト**：`tests/test_translation_note_position.py` は位置 × 形式のマトリクス（E2E の `marker+top|bottom|both` と `legacy+top|bottom|both` を含む）、複数行の接頭辞付与、byte-for-byte の後方互換性（golden literal）、sanitizer、frontmatter の分割（閉じられていない fence での送出を含む）、3段落形式、2段落 fallback、1段落 + Markdown リンクの guard、およびタイトルと URL が LLM に一切送信されないことを assert する重要な安全策 `TestLLMPayloadExcludesInvariants` を網羅。**190件のテストが成功**、regression は0件。
  - ドキュメント：badge を含む `README.md`（フランス語 + 14翻訳）、`CLAUDE.md`（pre-commit workflow + 詳細な CI 監視）、28翻訳を再生成
- **1.8** `--news` モード + 2026年モデルへの bump（2026-03-17、tag `v1.8`）：
  - デフォルトモデルを更新（2026年3月）：
    - OpenAI 高品質：`gpt-5` → `gpt-5.4`
    - OpenAI エコノミー：`gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 高品質：`gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - `gpt-5.4`、`gpt-5.4-mini`、`gpt-5.4-nano`（400k）および `gemini-3.1-pro-preview`（1M）の token limit を追加
  - 初期 `--news` モード：placeholder `#NEWSQUOTE\d+#` による英語引用の保護、`LANG_FLAGS` mapping（15言語）、対象言語別の flag 管理
  - 復元前に news placeholder を検証（regression：LLM が placeholder を削除すると、引用のない出力が暗黙的に生成されていた）
  - script `regen_translations.sh` を portable 化（絶対パス、pwd への依存なし）
  - README／CHANGELOG の language bar にフランス語リンクを追加し、28翻訳を再生成
- **1.7** 新機能：
  - 翻訳時に元のファイル名を維持する `--keep_filename` オプション
  - API key を自動的に読み込む `.env` ファイルのサポート
  - **inline code の維持**：翻訳中にバッククォート（`` `...` ``）を保護するように変更
  - system prompt の改善：
    - YAML frontmatter 内の引用符処理を改善
    - template variable `{variable}` を保護
    - 要求されていない翻訳者注記を禁止
  - 364ファイルでテスト成功（jls42.org のブログ移行）
- **1.6** 新機能：
  - 翻訳用 Google Gemini API のサポート（`--use_gemini`）
  - 2026年のデフォルトモデルに更新：
    - OpenAI：`gpt-5`（高品質）、`gpt-5-mini`（エコノミー）
    - Claude：`claude-sonnet-4-5`（高品質）、`claude-haiku-4-5`（エコノミー）
    - Gemini：`gemini-3-pro-preview`（高品質）、`gemini-3-flash-preview`（エコノミー）
  - より高速で低コストなモデルを使用するエコノミーモード（`--eco`）
  - ディレクトリを走査せずに単一ファイルを翻訳（`--file`）
  - 新しい簡略化された命名 pattern：`{base}-{lang}.md`
  - モデル名を含む旧形式を維持する `--include_model` オプション
  - 一覧にないモデルをデフォルトの token limit（128k）でサポート
  - README を14言語に翻訳
- **1.5** 改善：
  - **API key とデフォルトモデルの更新：**
    - **OpenAI：** `DEFAULT_MODEL_OPENAI` から `"gpt-4o"` に更新。
    - **Mistral AI：** `DEFAULT_MODEL_MISTRAL` から `"mistral-large-latest"` に更新。
    - **Anthropic Claude：** `DEFAULT_ANTHROPIC_API_KEY` を追加し、`DEFAULT_MODEL_CLAUDE` から `"claude-3-5-sonnet-20240620"` に更新。
  - **翻訳 prompt の最適化：**
    - 直接翻訳および翻訳注記用の prompt を拡充し、メタデータや特定の書式要素を維持するための詳細な指示を含めることで、明確性と効率を向上。
  - **コードの refactor：**
    - Mistral AI client の初期化で `MistralClient` を `Mistral` class に置換。
    - 可読性と保守性を高めるため import を再編成。
    - 翻訳時に元の書式を維持するため、テキストの segmentation と code block の処理を改善。
  - **出力ファイルの管理：**
    - 出力ファイル名内のモデルと言語の順序を反転（例：`f"{base}-{args.target_lang}-{args.model}.md"`）し、翻訳の整理と検索を容易化。
  - **その他の改善：**
    - 不要な空行を削除してコードを整理。
    - script の構造と可読性を向上させるための軽微な調整。
- **1.4** 新機能：
  - 翻訳用 Anthropic Claude API のサポート
  - 明確性と効率を高めるため prompt を最適化
  - コードの保守性を高めるための軽微な調整
- **1.3** 改善と新機能：
  - code block の処理を改善
  - 出力ファイルの管理を改善
  - 既存ファイルの検出を改善
  - 翻訳を強制する `--force` オプション
  - 出力ファイル名内のモデルと言語の順序を反転
- **1.2** changelog の修正
- **1.1** Mistral AI API のサポートを追加
- **1.0** 初期バージョン - OpenAI API をサポート

**gpt-5.6-solを使用してフランス語から日本語に翻訳された記事。**
