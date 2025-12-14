# Script 05 — Engineering Incident Review: Blameless Post-Mortem

## English

[Internal engineering review meeting]

FACILITATOR:
This meeting is a blameless post-mortem.  
Our goal is to understand what happened and how to prevent it in the future. [scope statement]

INCIDENT LEAD:
At 02:14 UTC, the service became unavailable for approximately twelve minutes.

ENGINEER A:
Logs confirm a memory spike immediately before the outage. [direct evidence]

ENGINEER B:
Based on metrics, the spike followed the deployment of the new caching layer. [inference]

FACILITATOR:
To be clear, we are identifying contributing factors, not assigning fault. [norm reinforcement]

INCIDENT LEAD:
The rollback procedure did not trigger automatically.

ENGINEER A:
That procedure requires a threshold that was not met. [mechanism explanation]

ENGINEER B:
We assumed the threshold was sufficient under all load conditions.

FACILITATOR:
That assumption appears to be incorrect. [assumption identification]

INCIDENT LEAD:
We have no evidence of malicious activity or operator error. [exclusion]

ENGINEER A:
Agreed. The system behaved as configured. [confirmation]

FACILITATOR:
Then the issue lies in the design, not in individual actions. [causal framing]

INCIDENT LEAD:
Action item: revise rollback thresholds and add additional monitoring. [forward action]

FACILITATOR:
Document that change and schedule a follow-up review. [process closure]

---

## Spanish

[Reunión interna de revisión técnica]

FACILITADOR:
Esta reunión es un análisis post-mortem sin culpables.  
Nuestro objetivo es entender lo ocurrido y prevenirlo en el futuro. [declaración de alcance]

LÍDER DEL INCIDENTE:
A las 02:14 UTC, el servicio quedó inactivo durante aproximadamente doce minutos.

INGENIERO A:
Los registros confirman un pico de memoria justo antes de la interrupción. [evidencia directa]

INGENIERO B:
Según las métricas, el pico ocurrió tras el despliegue de la nueva capa de caché. [inferencia]

FACILITADOR:
Para aclarar, identificamos factores contribuyentes, no culpables. [refuerzo normativo]

LÍDER DEL INCIDENTE:
El procedimiento de reversión no se activó automáticamente.

INGENIERO A:
Ese procedimiento depende de un umbral que no se alcanzó. [explicación del mecanismo]

INGENIERO B:
Asumimos que ese umbral era suficiente en todas las condiciones de carga.

FACILITADOR:
Esa suposición parece ser incorrecta. [identificación de suposición]

LÍDER DEL INCIDENTE:
No hay evidencia de actividad maliciosa ni de error humano. [exclusión]

INGENIERO A:
De acuerdo. El sistema actuó según su configuración. [confirmación]

FACILITADOR:
Entonces, el problema está en el diseño, no en las acciones individuales. [encuadre causal]

LÍDER DEL INCIDENTE:
Acción: revisar los umbrales de reversión y añadir monitoreo adicional. [acción futura]

FACILITADOR:
Documenten el cambio y programen una revisión de seguimiento. [cierre del proceso]

---

## French

[Réunion interne d’analyse technique]

FACILITATEUR :
Cette réunion est un post-mortem sans recherche de responsabilité.  
L’objectif est de comprendre l’incident et d’éviter sa répétition. [définition du cadre]

RESPONSABLE DE L’INCIDENT :
À 02 h 14 UTC, le service est devenu indisponible pendant environ douze minutes.

INGÉNIEUR A :
Les journaux confirment un pic de mémoire juste avant la panne. [preuve directe]

INGÉNIEUR B :
D’après les métriques, ce pic a suivi le déploiement de la nouvelle couche de cache. [inférence]

FACILITATEUR :
Nous identifions des facteurs contributifs, pas des fautes. [rappel de norme]

RESPONSABLE DE L’INCIDENT :
La procédure de retour arrière ne s’est pas déclenchée automatiquement.

INGÉNIEUR A :
Cette procédure dépend d’un seuil qui n’a pas été atteint. [explication du mécanisme]

INGÉNIEUR B :
Nous avons supposé que ce seuil était suffisant dans toutes les conditions de charge.

FACILITATEUR :
Cette hypothèse semble incorrecte. [identification d’hypothèse]

RESPONSABLE DE L’INCIDENT :
Aucune preuve d’activité malveillante ni d’erreur humaine. [exclusion]

INGÉNIEUR A :
Confirmé. Le système a fonctionné conformément à sa configuration. [confirmation]

FACILITATEUR :
Le problème relève donc de la conception, pas des actions individuelles. [cadre causal]

RESPONSABLE DE L’INCIDENT :
Action : ajuster les seuils de retour arrière et renforcer la surveillance. [action corrective]

FACILITATEUR :
Documentez ces changements et planifiez une revue de suivi. [clôture]

---

## Chinese (Simplified)

【内部工程复盘会议】

主持人：
本次会议为无责复盘。  
目标是理解发生了什么，并防止再次发生。【范围说明】

事件负责人：
在 02:14 UTC，服务中断约十二分钟。

工程师甲：
日志显示，在中断前出现了内存峰值。【直接证据】

工程师乙：
根据指标，该峰值发生在新缓存层部署之后。【推断】

主持人：
需要明确的是，我们识别的是促成因素，而不是责任。【规范强调】

事件负责人：
回滚流程未自动触发。

工程师甲：
该流程依赖的阈值未被触发。【机制说明】

工程师乙：
我们假设该阈值在所有负载条件下都足够。

主持人：
这一假设似乎不成立。【假设识别】

事件负责人：
没有发现恶意行为或人为错误的证据。【排除】

工程师甲：
同意。系统按配置运行。【确认】

主持人：
因此，问题在于设计，而非个人操作。【因果框定】

事件负责人：
行动项：调整回滚阈值并增加监控。【后续行动】

主持人：
请记录变更并安排后续复审。【流程结束】

---

## German

[Internes technisches Review-Meeting]

MODERATOR:
Dieses Treffen ist ein schuldloses Post-Mortem.  
Ziel ist es, den Vorfall zu verstehen und Wiederholungen zu verhindern. [Rahmenfestlegung]

INCIDENT-LEITER:
Um 02:14 UTC war der Dienst etwa zwölf Minuten nicht verfügbar.

INGENIEUR A:
Protokolle bestätigen einen Speicheranstieg unmittelbar vor dem Ausfall. [direkter Nachweis]

INGENIEUR B:
Den Metriken zufolge trat der Anstieg nach der Einführung der neuen Cache-Schicht auf. [Schlussfolgerung]

MODERATOR:
Zur Klarstellung: Wir benennen beitragende Faktoren, keine Schuldigen. [Normverstärkung]

INCIDENT-LEITER:
Das Rollback-Verfahren wurde nicht automatisch ausgelöst.

INGENIEUR A:
Dieses Verfahren hängt von einem Schwellenwert ab, der nicht erreicht wurde. [Mechanismuserklärung]

INGENIEUR B:
Wir gingen davon aus, dass dieser Schwellenwert unter allen Lastbedingungen ausreicht.

MODERATOR:
Diese Annahme war offenbar falsch. [Annahmenidentifikation]

INCIDENT-LEITER:
Es gibt keine Hinweise auf böswillige Aktivitäten oder Bedienfehler. [Ausschluss]

INGENIEUR A:
Einverstanden. Das System verhielt sich wie konfiguriert. [Bestätigung]

MODERATOR:
Damit liegt die Ursache im Design, nicht im individuellen Handeln. [Kausale Einordnung]

INCIDENT-LEITER:
Maßnahme: Anpassung der Rollback-Schwellen und zusätzliche Überwachung. [Folgeaktion]

MODERATOR:
Bitte dokumentieren und eine Nachbesprechung ansetzen. [Abschluss]

---

## Japanese

【社内エンジニアリング振り返り会議】

ファシリテーター：
本会議は非難を目的としないポストモーテムです。  
目的は原因を理解し、再発を防ぐことです。【範囲確認】

インシデント責任者：
02:14 UTC に、サービスが約12分間停止しました。

エンジニアA：
ログにより、停止直前のメモリ急増が確認されています。【直接証拠】

エンジニアB：
メトリクス上では、新しいキャッシュ層のデプロイ後に発生しています。【推論】

ファシリテーター：
要因の特定が目的であり、責任追及ではありません。【規範の再確認】

インシデント責任者：
ロールバックは自動で作動しませんでした。

エンジニアA：
設定された閾値に達していなかったためです。【仕組み説明】

エンジニアB：
その閾値で十分だと想定していました。

ファシリテーター：
その想定は誤りだったようです。【前提の特定】

インシデント責任者：
悪意ある行為や人的ミスの証拠はありません。【除外】

エンジニアA：
同意します。システムは設定通りに動作しました。【確認】

ファシリテーター：
つまり問題は設計にあり、個人の行動ではありません。【因果整理】

インシデント責任者：
対応項目：閾値の見直しと監視の追加。【是正措置】

ファシリテーター：
変更を記録し、再確認を予定してください。【終了】

---

## Arabic (MSA)

[اجتماع مراجعة هندسية داخلية]

المنسّق:
هذا الاجتماع هو مراجعة بلا إلقاء لوم.  
الهدف هو فهم ما حدث ومنع تكراره. [تحديد النطاق]

قائد الحادث:
في الساعة 02:14 بتوقيت UTC، توقف النظام لمدة اثنتي عشرة دقيقة تقريبًا.

المهندس أ:
تؤكد السجلات حدوث ارتفاع في الذاكرة قبل الانقطاع مباشرة. [دليل مباشر]

المهندس ب:
تشير المقاييس إلى أن الارتفاع تبع نشر طبقة التخزين المؤقت الجديدة. [استنتاج]

المنسّق:
نحن نحدد عوامل مساهمة، لا نبحث عن مسؤولين. [تعزيز القاعدة]

قائد الحادث:
لم يتم تفعيل إجراء التراجع تلقائيًا.

المهندس أ:
ذلك الإجراء يعتمد على حد لم يتم الوصول إليه. [شرح الآلية]

المهندس ب:
افترضنا أن هذا الحد كافٍ تحت جميع ظروف الحمل.

المنسّق:
يبدو أن هذا الافتراض غير صحيح. [تحديد الافتراض]

قائد الحادث:
لا توجد أدلة على نشاط خبيث أو خطأ بشري. [استبعاد]

المهندس أ:
موافق. النظام تصرف كما هو مهيأ. [تأكيد]

المنسّق:
بالتالي، المشكلة في التصميم وليس في الأفراد. [صياغة سببية]

قائد الحادث:
الإجراء التالي: تعديل الحدود وإضافة مراقبة إضافية. [إجراء لاحق]

المنسّق:
يرجى توثيق ذلك وتحديد مراجعة متابعة. [إغلاق]

---

## Portuguese (Brazil)

[Reunião interna de engenharia]

FACILITADOR:
Esta é uma análise pós-incidente sem atribuição de culpa.  
O objetivo é entender o ocorrido e evitar recorrência. [definição de escopo]

LÍDER DO INCIDENTE:
Às 02:14 UTC, o serviço ficou indisponível por cerca de doze minutos.

ENGENHEIRO A:
Os logs confirmam um pico de memória imediatamente antes da falha. [evidência direta]

ENGENHEIRO B:
Pelas métricas, o pico ocorreu após a implantação da nova camada de cache. [inferência]

FACILITADOR:
Estamos identificando fatores contribuintes, não responsáveis. [reforço normativo]

LÍDER DO INCIDENTE:
O procedimento de rollback não foi acionado automaticamente.

ENGENHEIRO A:
Esse procedimento depende de um limite que não foi atingido. [explicação do mecanismo]

ENGENHEIRO B:
Assumimos que esse limite era suficiente em todas as cargas.

FACILITADOR:
Essa suposição parece incorreta. [identificação de suposição]

LÍDER DO INCIDENTE:
Não há evidências de atividade maliciosa ou erro humano. [exclusão]

ENGENHEIRO A:
Concordo. O sistema operou conforme configurado. [confirmação]

FACILITADOR:
Logo, o problema está no design, não nas ações individuais. [enquadramento causal]

LÍDER DO INCIDENTE:
Ação: revisar limites de rollback e ampliar o monitoramento. [ação futura]

FACILITADOR:
Documentem as mudanças e agendem uma revisão posterior. [encerramento]

---

## Swahili (Kiswahili)

[Mkutano wa ndani wa mapitio ya uhandisi]

MSIMAMIZI:
Huu ni uchambuzi wa tukio bila kulaumu.  
Lengo ni kuelewa kilichotokea na kuzuia kutokea tena. [tamko la wigo]

KIONGOZI WA TUKIO:
Saa 02:14 UTC, huduma ilisimama kwa takriban dakika kumi na mbili.

MHANDISI A:
Rekodi zinaonyesha ongezeko la kumbukumbu kabla ya hitilafu. [ushahidi wa moja kwa moja]

MHANDISI B:
Kulingana na vipimo, ongezeko lilitokea baada ya kuweka safu mpya ya kache. [hitimisho]

MSIMAMIZI:
Tunatambua sababu zinazochangia, si lawama. [kuimarisha kanuni]

KIONGOZI WA TUKIO:
Utaratibu wa kurudisha haukuanzishwa kiotomatiki.

MHANDISI A:
Utaratibu huo hutegemea kizingiti ambacho hakikufikiwa. [maelezo ya mfumo]

MHANDISI B:
Tulidhani kizingiti hicho kinatosha chini ya hali zote za mzigo.

MSIMAMIZI:
Dhana hiyo inaonekana kuwa si sahihi. [utambuzi wa dhana]

KIONGOZI WA TUKIO:
Hakuna ushahidi wa nia mbaya au kosa la kibinadamu. [uondoaji]

MHANDISI A:
Nakubaliana. Mfumo ulifanya kazi kama ulivyosanidiwa. [uthibitisho]

MSIMAMIZI:
Hivyo basi, tatizo liko kwenye muundo, si kwa watu binafsi. [uundaji wa sababu]

KIONGOZI WA TUKIO:
Hatua: kurekebisha vizingiti na kuongeza ufuatiliaji. [hatua ya mbele]

MSIMAMIZI:
Tafadhali andikeni mabadiliko na pangenieni mapitio ya baadaye. [hitimisho]

---

## Lingua Sona – Latinized

[To be written]

---

## Lingua Sona – Sona Script

[To be written]


