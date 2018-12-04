#关闭的方式
* 在try中关闭
* 在finally中关闭
* 使用try()的方式

>把流定义在try()里,try,catch或者finally结束的时候，会自动关闭
>这种编写代码的方式叫做 try-with-resources， 这是从JDK7开始支持的技术。
>所有的流，都实现了一个接口叫做AutoCloseable
>任何类实现了这个接口，都可以在try()中进行实例化。 并且在try, catch, 
>finally结束的时候自动关闭，回收相关资源。

```java

package stream;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

public class TestStream {
    public static void main(String[] args) {
        File f = new File("d:/lol.txt");
        //把流定义在try()里,try,catch或者finally结束的时候，会自动关闭
        try (FileInputStream fis = new FileInputStream(f)) {
            byte[] all = new byte[(int) f.length()];
            fis.read(all);
            for (byte b : all) {
                System.out.println(b);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
 }

```
