# Week 1

*Prof. Nitin Chandrachoodan*  
*Department of EE, IIT Madras*  

*Notes by Adarsh (23f2003570)*  

## L2.1: Information Representation in a machine (18:30)

### Binary Representation

The **binary representation** of numbers uses only two digits: **0** and **1**. It is the basis of all digital systems, including computers, because electronic devices work with two states: on (1) and off (0).

#### Key Points:
- **Base-2 system**: Each digit in a binary number represents a power of 2. The rightmost digit is the least significant bit (2^0), and each digit to the left has a higher power of 2 (2^1, 2^2, etc.).
- **Example**:
   - Binary `1011` represents:
     \[
     1 \times 2^3 + 0 \times 2^2 + 1 \times 2^1 + 1 \times 2^0 = 8 + 0 + 2 + 1 = 11 \text{ in decimal}.
     \]
   
- **Converting from Decimal to Binary**:
   - Repeatedly divide the decimal number by 2, recording the remainder. The binary representation is formed by reading the remainders from bottom to top.
   - Example: Decimal `13` to binary:
$$
    13 \div 2 = 6 \text{ remainder } 1\\
    6 \div 2 = 3 \text{ remainder } 0\\
    3 \div 2 = 1 \text{ remainder } 1\\
    1 \div 2 = 0 \text{ remainder } 1\\
    \text{Binary } = 1101.
$$

Binary representation is fundamental for computer processing because all data (numbers, text, images) is ultimately stored and processed in binary form.

Negative numbers in binary are typically represented using **signed number representations**. The most common method is **two's complement**. Here are the main approaches to represent negative numbers in binary:

#### 1. **Sign-Magnitude Representation**
   - **Description**: The most significant bit (MSB) is used as a **sign bit**:
     - `0` indicates a positive number.
     - `1` indicates a negative number.
   - The remaining bits represent the magnitude (absolute value) of the number.
   - **Example**:
     - Positive `5` in 4-bit sign-magnitude: `0101`.
     - Negative `5` in 4-bit sign-magnitude: `1101`.
   - **Disadvantage**: It has two representations of zero (`+0` as `0000` and `-0` as `1000`), which complicates calculations.

#### 2. **One's Complement**
   - **Description**: In this method, negative numbers are obtained by flipping all the bits (changing `0` to `1` and `1` to `0`) of the positive number.
   - **Example**:
     - Positive `5` in 4-bit binary: `0101`.
     - Negative `5` in one's complement: `1010` (flipped bits).
   - **Disadvantage**: Like sign-magnitude, it has two representations for zero (`0000` for `+0` and `1111` for `-0`), leading to inefficiencies in arithmetic operations.

#### 3. **Two's Complement (Most Common Method)**
   - **Description**: Negative numbers are represented by taking the **one's complement** of the number and then **adding 1**.
   - **Advantages**:
     - It eliminates the problem of two zeros (there's only one zero).
     - Arithmetic operations (addition, subtraction) are easier to implement in hardware.
   - **Example**:
     - Positive `5` in 4-bit binary: `0101`.
     - To get `-5`:
       1. Find the one's complement: `1010`.
       2. Add `1` to the result: `1010 + 1 = 1011`.
     - Therefore, `-5` in 4-bit two's complement is `1011`.

#### 4. **Excess-N Representation (Bias Notation)**
   - **Description**: A bias (a fixed number) is added to the actual value to ensure that all numbers are represented as non-negative.
   - **Example**:
     - In **Excess-127** notation (for an 8-bit system), the value `127` is added to each number.
     - A number like `0` is represented as `127` (`01111111` in binary), and negative numbers are represented as smaller binary values.
   
---

#### Two's Complement in Detail
Two's complement is the most widely used system in modern computers due to its simplicity in hardware design. Here's an example of how to represent `-6` in 8-bit two's complement:

1. **Positive 6** in 8-bit binary: `00000110`.
2. **One's complement** of 6: `11111001` (flip all bits).
3. **Add 1** to the result: `11111001 + 1 = 11111010`.

Thus, `-6` is represented as `11111010` in 8-bit two's complement.

### Range of Two's Complement
For an **n-bit system**, the range of numbers represented in two's complement is:
- **Positive range**: \( 0 \) to \( 2^{n-1} - 1 \)
- **Negative range**: \( -2^{n-1} \) to \( -1 \)

For example, in an 8-bit system:
- Positive range: \( 0 \) to \( 127 \) (`01111111`).
- Negative range: \( -128 \) to \( -1 \) (`10000000` to `11111111`).

Two's complement makes arithmetic efficient, as addition and subtraction of positive and negative numbers follow the same procedure.


#### Points

1. A binary octet could be interpreted
   1. as a string of bits
   2. as a number
   3. as a character

### ASCII

**ASCII** (American Standard Code for Information Interchange) is a character encoding standard that represents text in computers and other devices. Each character (letter, digit, symbol, or control command) is assigned a unique **7-bit** binary number, which allows for **128 possible characters** (from 0 to 127). However, ASCII is often extended to 8 bits (1 byte), allowing for 256 possible characters (0 to 255) in what is known as **extended ASCII**.

#### ASCII Basics:
- Each character (e.g., 'A', 'b', '5', etc.) is mapped to a **binary number**.
- These binary values can be converted to **decimal** (base 10) or **hexadecimal** (base 16) values.
  
#### ASCII Ranges:

1. **Control Characters (0–31 and 127)**
   - These are non-printable characters used for controlling devices (like printers) and text formatting.
   - Examples:
     - `0`: Null (`NUL`)
     - `9`: Horizontal Tab (`TAB`)
     - `10`: Line Feed (`LF`)
     - `13`: Carriage Return (`CR`)
     - `27`: Escape (`ESC`)
     - `127`: Delete (`DEL`)

2. **Printable Characters (32–126)**
   - **32–47**: Symbols and punctuation marks.
     - Examples: `32` is a **space**, `33` is `!`, `44` is `,`, `47` is `/`.
   - **48–57**: **Numeric digits** (`0`–`9`).
     - Examples: `48` is `0`, `49` is `1`, `57` is `9`.
   - **58–64**: More punctuation marks.
     - Examples: `58` is `:`, `64` is `@`.
   - **65–90**: Uppercase **English letters** (`A`–`Z`).
     - Examples: `65` is `A`, `66` is `B`, `90` is `Z`.
   - **91–96**: More symbols.
     - Examples: `91` is `[`, `96` is `` ` ``.
   - **97–122**: Lowercase **English letters** (`a`–`z`).
     - Examples: `97` is `a`, `98` is `b`, `122` is `z`.
   - **123–126**: More punctuation marks.
     - Examples: `123` is `{`, `126` is `~`.

#### ASCII Table Example:

| Decimal | Hex  | Character | Binary   |
|---------|------|-----------|----------|
| 32      | 20   | (space)   | 00100000 |
| 48      | 30   | 0         | 00110000 |
| 65      | 41   | A         | 01000001 |
| 97      | 61   | a         | 01100001 |
| 127     | 7F   | DEL       | 01111111 |

#### **Extended ASCII (128–255)**
- Extends the standard ASCII by utilizing the full 8 bits, providing **128 additional characters**.
- It includes symbols, graphic characters, accented letters (used in other languages), and more control characters.
- Common in many systems but not universally standardized.
  
For example:
- `128–159`: More control characters.
- `160–255`: Additional characters, including accented letters (e.g., `é`, `ñ`), mathematical symbols, and graphical characters.

### Types of Text Encoding

**Text encoding** refers to the method of representing characters (letters, digits, symbols) as sequences of bytes. Different encoding schemes are used to represent text, especially as computers need to handle diverse scripts and symbols from various languages.

#### 1. **ASCII (American Standard Code for Information Interchange)**
   - **Bit Length**: 7 bits (commonly stored in 8 bits or 1 byte).
   - **Description**: ASCII is one of the oldest character encodings and represents **128 characters**, including control characters, numbers, uppercase and lowercase English letters, and basic symbols.
   - **Usage**: Mainly for basic English text and symbols.
   - **Limitations**: Cannot represent characters outside the basic English alphabet or certain control commands.
   - **Example**:
     - Character `'A'`: ASCII value `65` → Binary: `01000001`.

#### 2. **Extended ASCII**
   - **Bit Length**: 8 bits (1 byte).
   - **Description**: Extends the original ASCII to use the full byte (256 characters). The first 128 characters are the same as standard ASCII, while the additional 128 characters include special symbols, accented characters, and graphical characters.
   - **Usage**: Used for Western European languages that have accented characters (e.g., French, German).
   - **Example**:
     - Character `'é'`: Extended ASCII value `233`.

#### 3. **ISO 8859 (ISO Latin)**
   - **Bit Length**: 8 bits (1 byte).
   - **Description**: A family of encodings designed to support languages from different regions. For example:
     - **ISO-8859-1** (Latin-1) supports Western European languages.
     - **ISO-8859-5** supports Cyrillic.
   - **Usage**: Used for specific regional languages.
   - **Limitations**: It only supports 256 characters, so it is limited to certain languages per version.
   - **Example**:
     - ISO-8859-1 character `'ñ'` is `241`.

#### 4. **UTF-8 (Unicode Transformation Format - 8 bit)**
   - **Bit Length**: 1 to 4 bytes (variable length).
   - **Description**: The most widely used character encoding in the world today, **UTF-8** is backward-compatible with ASCII and can represent any character in the Unicode standard.
     - For ASCII characters (0–127), it uses 1 byte.
     - For larger Unicode characters, it uses up to 4 bytes.
   - **Usage**: Handles a wide range of languages and symbols, including emojis, making it the dominant encoding for the web and multi-language text.
   - **Advantages**: Efficient storage for ASCII characters while still being able to encode all Unicode characters.
   - **Example**:
     - Character `'A'`: UTF-8 value `65` (same as ASCII).
     - Character `'ñ'`: UTF-8 value `C3 B1` (2 bytes).

#### 5. **UTF-16 (Unicode Transformation Format - 16 bit)**
   - **Bit Length**: 2 or 4 bytes (variable length).
   - **Description**: Encodes Unicode characters using 2 bytes (16 bits) for most characters, but uses 4 bytes for characters outside the Basic Multilingual Plane (BMP), such as rare or historical scripts.
   - **Usage**: Often used in internal processing by systems that need to store large multilingual text, such as Windows or Java.
   - **Advantages**: More space-efficient for non-ASCII characters compared to UTF-8 but less efficient for ASCII.
   - **Example**:
     - Character `'A'`: UTF-16 value `0041` (2 bytes).
     - Character `'𐍈'` (Gothic letter): UTF-16 value `D800 DF48` (4 bytes).

#### 6. **UTF-32 (Unicode Transformation Format - 32 bit)**
   - **Bit Length**: 4 bytes (fixed length).
   - **Description**: Encodes each Unicode character as exactly 4 bytes, which allows for simple processing but results in higher storage costs.
   - **Usage**: Used when fixed-width encoding is needed, such as in some specialized systems or for internal representation where memory usage is less of a concern.
   - **Advantages**: Simple encoding with fixed length, making indexing characters easier.
   - **Disadvantages**: Not storage efficient; uses 4 bytes for every character, even simple ASCII ones.
   - **Example**:
     - Character `'A'`: UTF-32 value `00000041` (4 bytes).

#### 7. **Shift-JIS (Shift Japanese Industrial Standards)**
   - **Bit Length**: Variable length (1 or 2 bytes).
   - **Description**: A widely used encoding for representing Japanese characters. It combines single-byte representations for ASCII characters and double-byte representations for Japanese Kanji characters.
   - **Usage**: Primarily used in Japan for encoding Japanese text.
   - **Example**:
     - Character `'あ'` (Hiragana 'a'): Shift-JIS value `82 A0`.

#### 8. **Big5**
   - **Bit Length**: Variable length (1 or 2 bytes).
   - **Description**: Used for encoding **Traditional Chinese** characters. Like Shift-JIS, it uses single-byte sequences for ASCII characters and two-byte sequences for Chinese characters.
   - **Usage**: Primarily used in Taiwan and Hong Kong for representing Traditional Chinese.
   - **Example**:
     - Character `'你'` (You): Big5 value `A4A4`.

#### 9. **EBCDIC (Extended Binary Coded Decimal Interchange Code)**
   - **Bit Length**: 8 bits (1 byte).
   - **Description**: A character encoding developed by IBM for its mainframes. It is not compatible with ASCII or Unicode, using a different set of codes to represent characters.
   - **Usage**: Primarily used in older IBM mainframe and midrange systems.
   - **Example**:
     - Character `'A'`: EBCDIC value `C1`.

UCS2 is FIXED 2 bytes and UCS4 is fixed 4 bytes. Unlike UTF8 and other run length encoded formats these formats use fixed space sizes and is NOT optimized

More below

#### Summary of Text Encoding Types:
| Encoding Type | Bit Length   | Characters Supported | Use Cases                         |
|---------------|--------------|----------------------|-----------------------------------|
| **ASCII**     | 7 bits       | 128 characters        | Basic English text               |
| **Extended ASCII** | 8 bits  | 256 characters        | Western European languages       |
| **ISO 8859**  | 8 bits       | 256 characters        | Regional language support        |
| **UTF-8**     | 1 to 4 bytes | All Unicode           | Web, global language support     |
| **UTF-16** a.k.a **UCF2**   | 2 or 4 bytes | All Unicode           | Systems needing multilingual text|
| **UTF-32**  a.k.a **UCF4**  | 4 bytes      | All Unicode           | Internal representations         |
| **Shift-JIS** | 1 or 2 bytes | Japanese              | Japanese text                    |
| **Big5**      | 1 or 2 bytes | Traditional Chinese   | Traditional Chinese text         |
| **EBCDIC**    | 8 bits       | IBM systems characters| IBM mainframes                   |

Each encoding is suited to different use cases, depending on the language, system requirements, or memory constraints. **UTF-8** is the most common encoding today because of its efficiency and support for all characters in the Unicode standard.

### Universal Character Set

The **Universal Character Set (UCS)** is a standardized character encoding system that assigns a unique identifier, called a **code point**, to every character or symbol used in human languages, scripts, and technical symbols around the world. It is a **superset** of all character sets, aiming to include every character from all writing systems, past and present.

#### Key Aspects of UCS:
- **Part of the Unicode Standard**: UCS is essentially the same as the **Unicode standard**. The terms UCS and Unicode are often used interchangeably, though UCS is defined by the **ISO/IEC 10646** standard, while Unicode is managed by the Unicode Consortium.
- **Code Points**: Each character in UCS is assigned a **code point**, a unique numeric identifier, typically written in **hexadecimal** notation and prefixed with "U+". For example:
  - `'A'` is U+0041
  - `'é'` is U+00E9
  - `'你'` (Chinese character for "you") is U+4F60
  - Emoji `'😊'` is U+1F60A

#### Key Goals of UCS:
1. **Universal Coverage**: UCS seeks to include characters from all written scripts used by humans, as well as symbols used in various domains like mathematics, music, and technical communication.
2. **Consistency**: By assigning a unique code point to each character, UCS ensures that text can be encoded consistently and reliably across different platforms and applications.
3. **Compatibility**: It supports older encodings like ASCII, while also expanding to cover a wide range of languages and symbols not supported by legacy encodings.

#### UCS Code Space:
- **Planes**: UCS organizes characters into 17 **planes**, each with over 65,000 code points (ranging from U+0000 to U+10FFFF):
  - **Basic Multilingual Plane (BMP)**: Plane 0, which covers most commonly used characters (U+0000 to U+FFFF). It includes characters for scripts like Latin, Greek, Cyrillic, and many others.
  - **Supplementary Planes**: Include additional characters, like ancient scripts, emojis, and rare symbols.
    - Plane 1: **Supplementary Multilingual Plane (SMP)**.
    - Plane 2: **Supplementary Ideographic Plane (SIP)** for East Asian characters.
    - Plane 15 & 16: Reserved for **Private Use Areas**, where custom characters can be defined.

#### Relationship Between UCS and Unicode:
- **Unicode** and **UCS** share the same set of code points. However, Unicode specifies additional features like text handling, character properties, normalization, and algorithms for working with text (e.g., text rendering, bidirectional text).
- UCS provides the foundation (character code points), while Unicode offers practical rules and tools for text processing.

#### Character Encodings Based on UCS:
There are different ways to encode UCS characters into binary formats:
1. **UTF-8**: Variable-length encoding (1 to 4 bytes). Backward-compatible with ASCII, and the most popular encoding for web content.
2. **UTF-16**: Variable-length encoding (2 or 4 bytes). Common in some operating systems and applications.
3. **UTF-32**: Fixed-length encoding (4 bytes for every character). Simple, but uses more memory.

#### Summary (UCS):
The **Universal Character Set (UCS)** is the foundation of modern character encoding systems, ensuring that all written symbols from all languages, historical or contemporary, can be represented digitally. It is synonymous with the **Unicode Standard**, and its adoption enables seamless text exchange across different platforms, languages, and applications.

### Markup Languages

**Markup languages** are systems for annotating a document in a way that is distinguishable from the text itself. They use **tags** or **codes** embedded in the text to define how elements in the document should be structured, formatted, or presented. Markup languages do not typically provide any functionality for processing or manipulating data; instead, they describe the structure and format of text and data.

#### Key Characteristics:
1. **Tags or Elements**: Markup languages use tags, which are usually enclosed in angle brackets (`< >`), to mark sections of the document. These tags define the role of the text they enclose, such as a heading, paragraph, or link.
   - Example: `<h1>`, `<p>`, `<a>`, etc.
   
2. **Human-Readable**: The markup is generally readable by both humans and machines. A human can interpret what the tags mean, while a machine can process the tags to render or structure the content.
   
3. **Separation of Content and Formatting**: In a well-designed markup language, the text content and the instructions for rendering or structuring the text (i.e., the tags) are separate. This allows the same content to be presented in different ways by changing the markup.

#### Types of Markup Languages:

##### 1. **HTML (HyperText Markup Language)**
   - **Purpose**: The standard language used to create and structure content on the web. HTML provides the basic framework for a webpage, including headings, paragraphs, links, images, and more.
   - **Example**:
     ```html
     <html>
       <head>
         <title>My Web Page</title>
       </head>
       <body>
         <h1>Welcome to My Web Page</h1>
         <p>This is a paragraph of text.</p>
       </body>
     </html>
     ```

##### 2. **XML (eXtensible Markup Language)**
   - **Purpose**: A flexible, general-purpose markup language used to store and transport data. Unlike HTML, XML is designed to describe data rather than how it should be displayed.
   - **Example**:
     ```xml
     <book>
       <title>Database System Concepts</title>
       <author>Abraham Silberschatz</author>
       <year>2019</year>
     </book>
     ```

##### 3. **SGML (Standard Generalized Markup Language)**
   - **Purpose**: A highly flexible standard for defining the structure of documents. Both HTML and XML are derived from SGML. It allows users to define their own markup languages by specifying document structure and rules.
   - **Example**: SGML is not as widely used directly today, but it's the basis for HTML and XML.

##### 4. **Markdown**
   - **Purpose**: A lightweight markup language primarily used for formatting plain text in a simple, easy-to-read format. It's often used in readme files, documentation, and forums.
   - **Example**:
     ```markdown
     # My Document
     This is a **bold** word and this is *italic*.
     ```

##### 5. **LaTeX**
   - **Purpose**: A markup language used for typesetting complex documents, especially those with mathematical formulas and scientific content.
   - **Example**:
     ```latex
     \documentclass{article}
     \begin{document}
     \title{My First LaTeX Document}
     \author{Author Name}
     \maketitle
     \section{Introduction}
     This is the introduction.
     \end{document}
     ```

#### Types of Markup:
1. **Presentational Markup**: This type of markup describes how text should appear (its presentation). HTML initially followed this model, specifying things like font, color, and layout, although modern HTML separates content from style using CSS.
   - Example: `<b>` for bold text.

2. **Descriptive Markup**: This type of markup describes the meaning or structure of the content. XML is a prime example of descriptive markup, where tags represent what the data means, not how it should be displayed.
   - Example: `<title>` in XML describes the title of a book.

3. **Procedural Markup**: This markup includes instructions that direct the computer or processing software on how to perform certain operations. LaTeX is an example of a procedural markup language used to format documents.

#### Summary:
**Markup languages** are essential for structuring, formatting, and presenting documents or data. They separate content from presentation, allowing for consistent formatting and structure, making them foundational to web development (e.g., HTML) and data exchange (e.g., XML). Different markup languages are optimized for various use cases, from web content creation to scientific typesetting.


## L2.2 Efficiency of Encoding (20:34)

 Say you have a 1000 word document with 5 characters per word

 |Encoding|Calculation|Size|
 |-|-|-|
 |Extended ASCII (1 byte)|$1000 \times 5 \times 8$ bits|$40$ Kilobits|
 |UCS-4 (4 bytes)|$1000 \times 5 \times 4 \times 8$ bits|$160$ Kilobits|
 |ASCII (7 Bit)|$1000 \times 5 \times 7$|$35$ Kilobits|

 ### Web Encoding and Compression

 Web encoding algorithms like Huffman coding are used to compress data, making it smaller for storage and faster for transmission over networks. Here’s a breakdown of Huffman coding and a couple of other related concepts:

#### Huffman Coding

1. **Basic Concept**: Huffman coding is a lossless data compression algorithm. It assigns variable-length codes to input characters based on their frequencies. More frequent characters get shorter codes, while less frequent characters get longer codes.

2. **Process**:
   - **Frequency Analysis**: First, the algorithm counts how often each character appears in the data.
   - **Build a Tree**: It constructs a binary tree, where each leaf node represents a character. Characters are paired based on frequency, and the pair with the lowest frequency is merged into a new node. This process continues until there’s a single tree.
   - **Generate Codes**: The path from the root to each leaf node defines the binary code for that character (left branch = 0, right branch = 1).

3. **Advantages**:
   - Efficient for data with skewed frequency distributions (like text).
   - Lossless, meaning the original data can be perfectly reconstructed.

#### Other Encoding Algorithms

1. **Run-Length Encoding (RLE)**:
   - **Basic Concept**: This algorithm compresses data by replacing sequences of the same value with a single value and a count.
   - **Example**: Instead of storing "AAAABBBCCDAA", it would store "4A3B2C1D2A".

2. **Lempel-Ziv-Welch (LZW)**:
   - **Basic Concept**: This is a dictionary-based compression method that builds a dictionary of input sequences. When it finds a sequence that matches an entry in the dictionary, it replaces it with a reference to that entry.
   - **Usage**: Widely used in formats like GIF and ZIP.

##### Variable-Length Encoding

1. **Basic Concept**: In variable-length encoding, more common symbols are assigned shorter codes, while less frequent symbols are given longer codes. This optimizes the overall length of the encoded data.

2. **Examples**:
   - **Huffman Coding**: As discussed earlier, Huffman coding creates a binary tree based on character frequency, leading to variable-length codes.
   - **ASCII vs. UTF-8**: While ASCII uses fixed-length 7 or 8-bit codes, UTF-8 employs variable-length encoding to represent characters, using one to four bytes depending on the character.

3. **Advantages**:
   - **Space Efficiency**: Reduces the average code length, minimizing storage and transmission costs.
   - **Flexibility**: Can adapt to the distribution of data.

##### Other Similar Encodings

1. **Fixed-Length Encoding**:
   - **Concept**: Every symbol is represented by a code of the same length.
   - **Example**: ASCII uses 7 or 8 bits per character. This is simpler but less efficient for skewed distributions.

2. **Run-Length Encoding (RLE)**:
   - **Concept**: This method compresses data by replacing sequences of identical values with a single value and a count.
   - **Example**: "AAAABBBCCDAA" becomes "4A3B2C1D2A".
   - **Use Cases**: Effective for data with long runs of repeated values (e.g., simple images or text with repeated characters).

3. **Lempel-Ziv-Welch (LZW)**:
   - **Concept**: LZW is a dictionary-based compression technique. It builds a dictionary of sequences found in the data and replaces repeated sequences with references to the dictionary entries.
   - **Example**: Used in GIF and ZIP formats.
   - **Advantages**: Adapts to the data as it processes, making it efficient for a wide range of data types.

4. **Delta Encoding**:
   - **Concept**: This method stores the difference between sequential data points rather than the data points themselves. It’s particularly useful in time-series data.
   - **Example**: Instead of storing absolute values, it records changes (e.g., if values are 100, 102, 105, the deltas would be 100, 2, 3).

5. **Entropy Encoding**:
   - **Concept**: This is a broader category that includes variable-length encoding techniques like Huffman coding and arithmetic coding. It focuses on reducing redundancy based on the statistical properties of the input data.
   - **Example**: Arithmetic coding encodes entire messages as single numbers in a range, allowing for more efficient representation than fixed-length codes.


## L2.3 MArkup (13:19)
