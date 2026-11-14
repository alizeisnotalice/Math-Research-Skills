# R. L. Dobrushin (1967), “Shannon’s Theorems for Channels with Synchronization Errors”

- Source: Problems of Information Transmission 3(4), 11–26 (translation); original Russian journal pagination 18–36. Public full-text scan: https://www.mathnet.ru/php/getFT.phtml?jrnid=ppi&option_lang=eng&paperid=1919&what=fullt
- Reading status: partial. The PDF was read through its printed pages 18–24 (PDF pages 1–7); later pages were not inspected. The publisher/MathNet provides the full PDF, but the local curl attempt returned an access error, so no local copy is counted.
- Scope read: channel definition, assumptions, capacity formula and coding theorem statement; not the proof’s later sections.

## Exact result and hypotheses in the inspected pages

The channel is memoryless in the input-symbol index: each input letter independently produces a random finite output word, which may be empty. The decoder sees the concatenated output but not the input-symbol labels of its letters. The alphabets are finite. The paper assumes an exponential tail bound on the output-word length (equation (2.2)) and strictly positive finite mean output length. Theorem 1 states a coding theorem at rates below a capacity C, with a converse above C, and defines C as the limit of C_n/n, where C_n is the supremum of mutual information between the n-letter input word and its concatenated output over input distributions (equations (2.6)–(2.7), PDF pp. 2–3; printed pp. 19–20).

This model contains an i.i.d. deletion channel as the special case where each input bit either produces itself or the empty word. It establishes why capacity is normalized per input symbol even though output length is random. It is not a theorem about general renewal-arrival queues or about all stationary channel models.

## Proof chain and limits

The stated proof idea adds sparse resynchronization markers at a growing interval: the marker overhead vanishes per input symbol while the auxiliary synchronization information allows an information-stability argument. The inspected text does not include the full proof, so this note does not reconstruct its detailed estimates or verify the hypotheses against a new channel.

## Migration gap

When applying the result to a new synchronization channel, verify independent per-input-symbol output words, finite mean and exponential tail of word length, and the precise coding criterion. Do not silently replace the missing input indices by an ordinary memoryless channel output.
