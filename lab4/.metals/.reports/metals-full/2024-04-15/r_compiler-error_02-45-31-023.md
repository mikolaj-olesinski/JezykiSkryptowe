file://<WORKSPACE>/zad4.java
### java.util.NoSuchElementException: next on empty iterator

occurred in the presentation compiler.

presentation compiler configuration:
Scala version: 3.3.1
Classpath:
<HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala3-library_3/3.3.1/scala3-library_3-3.3.1.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala-library/2.13.10/scala-library-2.13.10.jar [exists ]
Options:



action parameters:
offset: 2629
uri: file://<WORKSPACE>/zad4.java
text:
```scala
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;

public class zad4 {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Złe argumenty wpisane");
            return;
        }

        String fileName = args[0];
        int charCount = 0;
        int wordCount = 0;
        int lineCount = 0;
        Map<String, Integer> wordFrequency = new HashMap<>();
        Map<Character, Integer> charFrequency = new HashMap<>();

        try {
            for (String line : Files.readAllLines(Paths.get(fileName))) {
                lineCount++;
                String[] words = line.split("\\s+");

                for (String word : words) {
                    if (word.isEmpty()) continue; //zakladam ze puste slowa nie sa liczone
                    wordCount++;
                    wordFrequency.put(word, wordFrequency.getOrDefault(word, 0) + 1);
                }
                for (char c : line.toCharArray()) {
                    if (Character.isWhitespace(c)) continue; //zakladam ze biale znaki nie sa liczone
                    charCount++;
                    charFrequency.put(c, charFrequency.getOrDefault(c, 0) + 1);
                }
            }
        } catch (IOException e) {
            throw new RuntimeException("Błąd odczytu pliku", e);
        }

        char mostFrequentChar = '\0'; // null character
        int maxCharFrequency = 0;
        for (Map.Entry<Character, Integer> entry : charFrequency.entrySet()) {
            if (entry.getValue() > maxCharFrequency) {
                mostFrequentChar = entry.getKey();
                maxCharFrequency = entry.getValue();
            }
        }

        String mostFrequentWord = null;
        int maxWordFrequency = 0;
        for (Map.Entry<String, Integer> entry : wordFrequency.entrySet()) {
            if (entry.getValue() > maxWordFrequency) {
                mostFrequentWord = entry.getKey();
                maxWordFrequency = entry.getValue();
            }
        }

        

        StringBuilder jsonResult = new StringBuilder();
        jsonResult.append("{\n");
        jsonResult.append("  \"filePath\": \"" + fileName + "\",\n");
        jsonResult.append("  \"charCount\": " + charCount + ",\n");
        jsonResult.append("  \"wordCount\": " + wordCount + ",\n");
        jsonResult.append("  \"lineCount\": " + lineCount + ",\n");
        jsonResult.append("  \"mostFrequentChar\": \"" + mostFrequentChar + "\",\n");
        jsonResult.append("  \"mostFrequentWord\": \"" + mostFrequen@@tWord + "\"\n");
        jsonResult.append("}\n");

        System.out.println(jsonResult.toString());
    }
}

```



#### Error stacktrace:

```
scala.collection.Iterator$$anon$19.next(Iterator.scala:973)
	scala.collection.Iterator$$anon$19.next(Iterator.scala:971)
	scala.collection.mutable.MutationTracker$CheckedIterator.next(MutationTracker.scala:76)
	scala.collection.IterableOps.head(Iterable.scala:222)
	scala.collection.IterableOps.head$(Iterable.scala:222)
	scala.collection.AbstractIterable.head(Iterable.scala:933)
	dotty.tools.dotc.interactive.InteractiveDriver.run(InteractiveDriver.scala:168)
	scala.meta.internal.pc.MetalsDriver.run(MetalsDriver.scala:45)
	scala.meta.internal.pc.HoverProvider$.hover(HoverProvider.scala:34)
	scala.meta.internal.pc.ScalaPresentationCompiler.hover$$anonfun$1(ScalaPresentationCompiler.scala:352)
```
#### Short summary: 

java.util.NoSuchElementException: next on empty iterator