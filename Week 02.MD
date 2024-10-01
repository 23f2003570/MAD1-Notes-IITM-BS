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


## L2.3 Markup (13:19)

Markup languages are systems for annotating a document in a way that is syntactically distinguishable from the text. They provide a means to structure, format, and present content, often using tags or special characters. 

Common features include:

1. **Tags**: Elements enclosed in angle brackets (e.g., `<tag>`), which indicate the start and end of a content segment.
2. **Attributes**: Additional information about an element, often included within the opening tag (e.g., `<tag attribute="value">`).
3. **Hierarchical Structure**: Elements can be nested within one another, creating a tree-like structure that defines the document's organization.

Popular markup languages include:

- **HTML (HyperText Markup Language)**: Used for creating web pages and applications.
- **XML (eXtensible Markup Language)**: A flexible format for storing and transporting data.
- **Markdown**: A lightweight markup language for formatting plain text, commonly used in documentation and web content.
- **LaTeX** is a markup


### Types of Markups

1. Presentational Markup
   1. **WYSIWYG**
      1. In computing, WYSIWYG , an acronym for what you see is what you get, refers to software that allows content to be edited in a form that resembles its appearance when printed or displayed as a finished product, such as a printed document, web page, or slide presentation.
   2. Markdown
   3. HTML
2. Procedural Markup
   1. goes into the details of how to display the text! Don't get confused with Presentational Markup. This topic has not been lectured in detail.
   2. HTML is NOT a Procedural Markup
   3. TeX, LaTeX, Nroff, PostScript are procedural markups.
   4. Basically describes the steps on how to display text
      1. Change font to large/bold `<h1><bold>Font</bold></h1>`
      2. Skip 2 lines, indent 2 columns
   
Markup can be categorized into several types based on its purpose and functionality.

#### 1. **Presentational Markup**
This type of markup focuses on the appearance and layout of the content.

- **Example**: HTML (HyperText Markup Language) is primarily presentational. It structures content for display in web browsers using tags like `<h1>`, `<p>`, and `<div>`, which define how the content should look.

#### 2. **Descriptive Markup**
Descriptive markup provides metadata about the content, focusing on its meaning rather than its presentation. It specifies the meaning of the content rather than how it should be displayed

- **Example**: XML (eXtensible Markup Language) is a descriptive markup language used to define custom data structures. It describes data and its relationships without specifying how it should be presented.
- `<title>`, `<heading>`, `<paragraph>`
- Has an effect on the visual.

#### 3. **Semantic Markup**
Semantic markup conveys meaning and context about the content, which can enhance accessibility and improve search engine optimization (SEO).

- **Example**: HTML5 includes semantic elements like `<article>`, `<section>`, and `<header>`, which provide clear context about the content's role in a web page.

#### 4. **Structural Markup**
This type defines the organization and structure of a document, outlining how different sections relate to each other.

- **Example**: Markdown is a lightweight markup language that structures text with simple syntax (like `#` for headers). It focuses on the logical organization of content rather than its presentation.
- `<body>`, `<html>` are structural markups.

#### 5. **Interchange Markup**
Interchange markup languages facilitate the exchange of information between systems.

- **Example**: JSON (JavaScript Object Notation) is used for data interchange in APIs and web applications, providing a structured format for data transfer, though it is not a traditional markup language.

#### 6. **Formatting Markup**
This type allows for fine control over the presentation of text and other elements.

- **Example**: LaTeX is a markup language often used for typesetting documents, particularly in academia. It allows precise control over formatting and is widely used for mathematical and scientific documents.

#### 7. **Hybrid Markup**
Some languages combine features of various markup types to achieve more complex functionality.

- **Example**: XHTML (eXtensible HyperText Markup Language) blends the rules of XML with HTML, allowing for more rigorous syntax while maintaining web page functionality.

### Procedural Markup

Procedural markup is a type of markup language that not only describes the structure and presentation of content but also includes instructions or procedures for how to process or manipulate that content. It often specifies how elements should be handled by a processor or interpreter, which can include commands for rendering, data manipulation, or logic-based actions.

#### Key Features of Procedural Markup:

1. **Instructions**: Procedural markup languages include commands that direct how the content should be processed, often in a specific order or under certain conditions.

2. **Control Flow**: They can incorporate programming constructs such as loops, conditionals, and variables, allowing for dynamic content generation and more complex interactions.

3. **Contextual Processing**: The markup often relies on a processing engine that interprets the instructions and generates the final output, which could be formatted text, interactive content, or structured data.

#### Examples:

- **LaTeX**: While primarily a typesetting system, LaTeX allows for procedural elements in its commands (e.g., conditionals, loops) to control the formatting and layout of documents dynamically.

- **XSLT (eXtensible Stylesheet Language Transformations)**: Used to transform XML documents into other formats (like HTML), XSLT allows for procedural instructions on how to process XML data.

- **Tcl (Tool Command Language)**: Often used in conjunction with other markup or scripting languages, Tcl provides a way to embed commands that control processing.

#### Use Cases:
Procedural markup is useful in contexts where content needs to be generated or manipulated dynamically, such as:

- Generating reports from data sources.
- Creating interactive web content.
- Processing data for presentations.

## L2.4 Introduction to HTML (23:36)

### Notes on HTML (HyperText Markup Language)

#### 1. **Definition**
HTML is the standard markup language used to create and design documents on the web. It structures content and specifies how elements should be displayed in web browsers.

#### 2. **Basic Structure**
An HTML document has a specific structure that includes:
- **DOCTYPE Declaration**: Specifies the version of HTML (e.g., `<!DOCTYPE html>` for HTML5).
- **HTML Element**: The root element that wraps all content (`<html>`).
- **Head Section**: Contains metadata, title, links to stylesheets, and scripts (`<head>`).
- **Body Section**: Contains the actual content that is displayed on the web page (`<body>`).

#### 3. **Common Elements**
- **Headings**: Defined with `<h1>` to `<h6>`, where `<h1>` is the highest level.
- **Paragraphs**: Created using `<p>`.
- **Links**: Hyperlinks are created with the `<a>` tag (e.g., `<a href="url">link text</a>`).
- **Images**: Inserted using the `<img>` tag (e.g., `<img src="image.jpg" alt="description">`).
- **Lists**: Ordered lists (`<ol>`) and unordered lists (`<ul>`) are used to create lists.
  - `<ol>` for lists with alphabets, romans, numbers
  - `<ul>` for bullets, squares, circle, disc, dot
- **Tables**: Created using `<table>`, with rows (`<tr>`) and cells (`<td>` for data, `<th>` for headers).

#### 4. **Attributes**
HTML elements can have attributes that provide additional information:
- **Common Attributes**: `id`, `class`, `style`, `src`, `href`, `alt`, etc.
- **Global Attributes**: Can be used on any HTML element (e.g., `data-*` attributes, `role`, `tabindex`).

#### 5. **Semantic HTML**
Using elements that convey meaning about the content, such as:
- `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`.
- Enhances accessibility and SEO by providing context to search engines and assistive technologies.

#### 6. **Forms and Input**
HTML forms allow users to input data:
- **Form Element**: Defined using `<form>`.
- **Input Types**: Various input fields (`<input type="text">`, `<input type="radio">`, `<textarea>`, etc.).
- **Buttons**: Created using `<button>` or `<input type="submit">`.

#### 7. **HTML5 Features**
HTML5 introduced several new features and APIs:
- **New Elements**: `<article>`, `<section>`, `<aside>`, `<figure>`, `<figcaption>`.
- **Audio and Video**: `<audio>` and `<video>` tags for multimedia content.
- **Canvas**: The `<canvas>` element for drawing graphics via scripting (JavaScript).
- **Local Storage**: API for storing data locally within the user's browser.

#### 8. **Accessibility**
Best practices to ensure web content is accessible:
- Use appropriate semantic elements.
- Provide alternative text for images.
- Ensure forms are properly labeled.
- Use ARIA (Accessible Rich Internet Applications) roles and properties when necessary.

#### 9. **Best Practices**
- Keep HTML clean and well-structured.
- Use comments (`<!-- Comment -->`) to annotate the code.
- Validate HTML using tools like the W3C Validator to ensure compliance with standards.
- Separate content (HTML) from presentation (CSS) and behavior (JavaScript).


### List of All HTML5 Tags

| **Tag**          | **Description**                                         |
|------------------|---------------------------------------------------------|
| `<a>`            | Defines a hyperlink to another document or resource.    |
| `<abbr>`         | Represents an abbreviation or acronym.                  |
| `<address>`      | Provides contact information for the author or owner of a document. |
| `<area>`         | Defines a clickable area within an image map.           |
| `<article>`      | Represents a self-contained piece of content, like a news article or blog post. |
| `<aside>`        | Contains content related to the main content, like a sidebar. |
| `<audio>`        | Embeds audio content, allowing playback directly in the browser. |
| `<b>`            | Makes text bold without conveying importance.           |
| `<base>`         | Specifies a base URL for all relative URLs in a document. |
| `<bdi>`          | Isolates a section of text that may be formatted in a different direction from other text. |
| `<bdo>`          | Overrides the current text direction.                   |
| `<blockquote>`   | Represents a section that is quoted from another source. |
| `<body>`         | Contains the content of the document.                   |
| `<br>`           | Inserts a line break.                                   |
| `<button>`       | Represents a clickable button.                           |
| `<canvas>`       | Used for drawing graphics via scripting (JavaScript).   |
| `<caption>`      | Specifies a caption for a table.                        |
| `<cite>`         | Represents the title of a creative work.                |
| `<code>`         | Displays a single line of code or code snippet.         |
| `<col>`          | Specifies column properties for an HTML table.          |
| `<colgroup>`     | Groups a set of one or more columns in a table.        |
| `<data>`         | Links a content with a machine-readable value.          |
| `<datalist>`     | Contains a set of predefined options for input controls. |
| `<dd>`           | Describes a term in a description list.                 |
| `<del>`          | Represents text that has been deleted from a document.   |
| `<details>`      | A disclosure widget from which the user can obtain additional information. |
| `<dfn>`          | Indicates the defining instance of a term.              |
| `<dialog>`       | Represents a dialog box or other interactive component.  |
| `<div>`          | Defines a division or section in a document.            |
| `<dl>`           | Represents a description list.                           |
| `<dt>`           | Defines a term/name in a description list.              |
| `<em>`           | Emphasizes text, typically displayed in italics.       |
| `<embed>`        | Embeds external content, such as multimedia.            |
| `<fieldset>`     | Groups related elements in a form.                       |
| `<figcaption>`   | Provides a caption for the `<figure>` element.         |
| `<figure>`       | Represents content that is referenced from the main content. |
| `<footer>`       | Defines the footer for a section or page.               |
| `<form>`         | Represents a section for user input.                     |
| `<h1>` to `<h6>` | Define headings, with `<h1>` as the highest level and `<h6>` as the lowest. |
| `<head>`         | Contains metadata and links to scripts and styles.      |
| `<header>`       | Represents introductory content for a section or page.  |
| `<hr>`           | Inserts a horizontal rule (line) in the document.       |
| `<html>`         | The root element of an HTML document.                    |
| `<i>`            | Represents text in an alternate voice or mood.          |
| `<iframe>`       | Embeds another document within the current HTML document. |
| `<img>`          | Embeds an image in the document.                         |
| `<input>`        | Represents an input field within a form.                |
| `<ins>`          | Represents text that has been inserted into a document.  |
| `<kbd>`          | Represents user input, typically keyboard input.        |
| `<label>`        | Defines a label for an input element.                   |
| `<legend>`       | Provides a caption for a `<fieldset>`.                  |
| `<li>`           | Defines a list item in an ordered or unordered list.    |
| `<link>`         | Links to external resources like stylesheets.           |
| `<main>`         | Represents the main content of the document.             |
| `<map>`          | Defines an image map.                                    |
| `<mark>`         | Highlights text for reference or emphasis.              |
| `<meta>`         | Provides metadata about the document.                    |
| `<meter>`        | Represents a scalar measurement within a known range.   |
| `<nav>`          | Contains navigation links for the document.             |
| `<noscript>`     | Provides alternate content for users who have disabled scripts. |
| `<object>`       | Represents an external resource, such as multimedia.    |
| `<ol>`           | Defines an ordered list.                                 |
| `<optgroup>`     | Groups related options within a `<select>` dropdown.   |
| `<option>`       | Defines an option in a dropdown list.                   |
| `<output>`       | Represents the result of a calculation or user action.  |
| `<p>`            | Defines a paragraph.                                    |
| `<param>`        | Defines parameters for an `<object>` element.           |
| `<picture>`      | Provides a responsive image with multiple source options.|
| `<pre>`          | Displays preformatted text, preserving whitespace and line breaks. |
| `<progress>`     | Represents the progress of a task, typically displayed as a progress bar. |
| `<q>`            | Represents a short inline quotation.                     |
| `<rp>`           | Provides fallback text for browsers that do not support ruby annotations. |
| `<rt>`           | Defines a ruby text component for East Asian typography. |
| `<ruby>`         | Represents a ruby annotation, providing pronunciation guides. |
| `<s>`            | Represents text that is no longer accurate or relevant. |
| `<samp>`         | Represents sample output from a computer program.       |
| `<script>`       | Embeds JavaScript in the document.                      |
| `<section>`      | Defines a section of related content.                   |
| `<select>`       | Creates a dropdown list for selecting options.          |
| `<small>`        | Renders text in a smaller size, typically for fine print.|
| `<source>`       | Specifies multiple media resources for elements like `<video>` and `<audio>`. |
| `<span>`         | A generic inline container for text and other elements. |
| `<strong>`       | Represents important text, typically displayed in bold. |
| `<style>`        | Contains CSS styles for the document.                   |
| `<sub>`          | Displays text as subscript.                             |
| `<summary>`      | Provides a summary for the `<details>` element.        |
| `<sup>`          | Displays text as superscript.                           |
| `<table>`        | Defines a table.                                        |
| `<tbody>`        | Groups the body content in a table.                     |
| `<td>`           | Defines a cell in a table.                              |
| `<template>`     | Represents a template that can be cloned and used in the document. |
| `<textarea>`     | Creates a multi-line text input field.                  |
| `<tfoot>`        | Groups the footer content in a table.                   |
| `<th>`           | Defines a header cell in a table.                       |
| `<thead>`        | Groups the header content in a table.                   |
| `<time>`         | Represents a specific time or date.                     |
| `<title>`        | Defines the title of the document, shown in the browser's title bar. |
| `<tr>`           | Defines a row in a table.                               |
| `<track>`        | Specifies text tracks for `<video>` and `<audio>` elements. |
| `<u>`            | Represents text that is unarticulated or in need of highlighting. |
| `<ul>`           | Defines an unordered list.                               |
| `<var>`          | Represents a variable in a mathematical expression or programming context. |
| `<video>`        | Embeds a video file, allowing playback directly in the browser. |
| `<wbr>`          | Suggests a line break opportunity.                      |

This table includes the most commonly used HTML5 tags along with a brief description of each, which can help in understanding their purpose and usage in web development.


### Logical Markups in HTML5

**NOTE** this is not complete.. Please refer to https://developer.mozilla.org/en-US/docs/Web/HTML/Element


| **Tag**          | **Description**                                         |
|------------------|---------------------------------------------------------|
| `<article>`      | Represents a self-contained piece of content, like a news article or blog post. |
| `<aside>`        | Contains content related to the main content, often displayed as a sidebar. |
| `<details>`      | A disclosure widget that the user can open to access additional information. |
| `<figcaption>`   | Provides a caption for the `<figure>` element.         |
| `<figure>`       | Represents content that is referenced from the main content, such as images or diagrams. |
| `<footer>`       | Defines the footer for a section or page, often containing metadata or links. |
| `<header>`       | Represents introductory content, typically containing navigational links or headings. |
| `<main>`         | Represents the main content of the document, excluding headers, footers, and sidebars. |
| `<mark>`         | Highlights text for reference or emphasis.             |
| `<nav>`          | Contains navigation links for the document.            |
| `<section>`      | Defines a thematic grouping of content, typically with a heading. |
| `<summary>`      | Provides a summary for the `<details>` element, visible when the details are closed. |
| `<time>`         | Represents a specific time or date, often with machine-readable formats. |

These logical markup elements enhance the semantic structure of web content, improving accessibility, search engine optimization, and the overall clarity of the document's structure.


### Accessibility

HTML5 introduces several elements and attributes that enhance accessibility, making web content more usable for people with disabilities

#### 1. **Semantic Elements**
Using semantic HTML elements improves accessibility by providing context to assistive technologies (like screen readers):

- **Structural Elements**:
  - `<header>`: Defines introductory content or navigational links.
  - `<nav>`: Contains navigation links, helping users find their way through the content.
  - `<main>`: Represents the main content of the document, excluding headers and footers.
  - `<section>`: Defines a thematic grouping of content, making it easier for screen readers to navigate.
  - `<article>`: Represents independent content that can be reused elsewhere, enhancing clarity.
  - `<footer>`: Contains footer content for sections or pages, providing additional context.

#### 2. **Form Elements**
HTML5 offers better accessibility for forms:

- **Labels**: Use `<label>` elements to associate labels with input fields. This improves usability, especially for screen reader users.
- **Input Types**: HTML5 introduces various input types (e.g., `type="email"`, `type="date"`) that provide built-in validation and enhance user experience.
- **ARIA Attributes**: Use ARIA (Accessible Rich Internet Applications) attributes (like `aria-labelledby` and `aria-describedby`) to provide additional context for form elements.

#### 3. **Text and Content Elements**
Proper use of text elements can enhance accessibility:

- **Headings**: Use `<h1>` to `<h6>` to create a logical hierarchy of headings, making it easier for users to understand the structure of the content.
- **Emphasis and Importance**: Use `<strong>` for important text and `<em>` for emphasized text, as these tags convey meaning to assistive technologies.

#### 4. **Media Elements**
HTML5 provides tags for multimedia content:

- **Images**: Always include `alt` attributes in `<img>` tags to provide descriptive text for images, ensuring that screen reader users can understand the content.
- **Audio and Video**: Use `<audio>` and `<video>` elements with captions or transcripts to make multimedia content accessible to all users.
- **Track Element**: Use the `<track>` element within `<video>` or `<audio>` for subtitles or captions, enhancing understanding for deaf or hard-of-hearing users.

#### 5. **Navigation and Landmarks**
Landmark roles help users navigate:

- Use ARIA roles (like `role="navigation"` or `role="banner"`) to define landmarks, making it easier for screen reader users to skip to relevant sections.
- `<nav>`, `<header>`, and `<footer>` automatically have landmark roles, improving accessibility without additional ARIA attributes.

#### 6. **Best Practices**
To ensure optimal accessibility:

- **Test with Assistive Technologies**: Regularly test your website with screen readers and other assistive technologies to identify potential accessibility issues.
- **Use Clear Language**: Write in clear, simple language, and use headings and lists to organize content effectively.
- **Keyboard Navigation**: Ensure all interactive elements are accessible via keyboard navigation, as some users cannot use a mouse.
- **Consistent Structure**: Maintain a consistent layout and navigation structure throughout the site to aid user orientation.

#### 7. **Conclusion**
By using HTML5 accessibility tags and following best practices, web developers can create inclusive web experiences that are usable by everyone, regardless of their abilities. Prioritizing accessibility not only improves user experience but also adheres to legal standards and ethical considerations.

### Document Object Model

The Document Object Model (DOM) is a programming interface for HTML and XML documents. It represents the document structure as a tree of objects, enabling dynamic manipulation of the document's content, structure, and style. Here are key concepts and features related to the HTML5 DOM:

#### 1. **Understanding the DOM**
- **Tree Structure**: The DOM represents the HTML document as a tree, where each element (tags, text, attributes) is a node in that tree. The document itself is the root node, with child nodes representing elements and text.
- **Node Types**: The DOM categorizes nodes into several types:
  - **Element Nodes**: Correspond to HTML elements (e.g., `<div>`, `<p>`).
  - **Text Nodes**: Contain the text content of elements.
  - **Attribute Nodes**: Represent attributes of elements (though often accessed through element nodes).
  - **Comment Nodes**: Represent comments in the markup.

#### 2. **Accessing DOM Elements**
- **Document Object**: The `document` object is the entry point for interacting with the DOM.
- **Methods to Access Elements**:
  - `document.getElementById(id)`: Returns the element with the specified ID.
  - `document.getElementsByClassName(className)`: Returns a live HTMLCollection of elements with the specified class name.
  - `document.getElementsByTagName(tagName)`: Returns a live HTMLCollection of elements with the specified tag name.
  - `document.querySelector(selector)`: Returns the first element that matches the specified CSS selector.
  - `document.querySelectorAll(selector)`: Returns a static NodeList of all matching elements.

#### 3. **Manipulating the DOM**
- **Creating Elements**: Use `document.createElement(tagName)` to create a new element.
- **Appending Elements**: Use methods like `appendChild()` or `insertBefore()` to add new nodes to the document.
- **Removing Elements**: Use `removeChild()` to remove a node from its parent.
- **Modifying Attributes**: Use `setAttribute(attr, value)` and `getAttribute(attr)` to modify or retrieve element attributes.

#### 4. **Event Handling**
- **Adding Event Listeners**: Use `element.addEventListener(event, function)` to respond to user interactions, such as clicks or key presses.
- **Removing Event Listeners**: Use `element.removeEventListener(event, function)` to detach an event listener.

#### 5. **Dynamic Updates**
- The DOM allows for real-time updates to the document, enabling developers to create interactive web applications.
- Use JavaScript to modify content, change styles, or create animations based on user input or other events.

#### 6. **Browser Compatibility**
- The DOM is standardized across modern browsers, but some methods and properties may vary. Always check compatibility when using newer features.
- Utilize feature detection (e.g., using libraries like Modernizr) to ensure functionality across different browsers.

#### 7. **Performance Considerations**
- Frequent DOM manipulations can lead to performance issues. Batch updates or use Document Fragments to minimize reflows and repaints.
- Use `requestAnimationFrame` for animations to improve performance and rendering efficiency.
  
### Block and Inline Tags in HTML

HTML elements can be categorized into two main types based on how they are rendered in the browser: **block-level elements** and **inline elements**. Understanding the difference between these two types is essential for effective web layout and design.

#### 1. **Block-Level Elements**

**Definition**: Block-level elements occupy the full width of their parent container, starting on a new line. They create a "block" of content.

**Characteristics**:
- Always start on a new line.
- Stretch out to the full width available (unless a specific width is set).
- Can contain other block-level elements and inline elements.

**Common Block-Level Elements**:
- `<div>`: A generic container for grouping content.
- `<p>`: Represents a paragraph of text.
- `<h1>` to `<h6>`: Heading elements, with `<h1>` being the highest level.
- `<ul>`: Unordered list.
- `<ol>`: Ordered list.
- `<li>`: List item (used inside `<ul>` or `<ol>`).
- `<header>`: Represents introductory content for a section.
- `<footer>`: Defines the footer for a section or page.
- `<section>`: Represents a thematic grouping of content.
- `<article>`: Represents self-contained content that could stand alone.

**Usage Example**:
```html
<div>
    <h1>Main Title</h1>
    <p>This is a paragraph.</p>
</div>
```

#### 2. **Inline Elements**

**Definition**: Inline elements do not start on a new line and only take up as much width as necessary. They flow within the surrounding text.

**Characteristics**:
- Do not start on a new line.
- Only occupy the space necessary for their content.
- Can contain only inline elements (not block-level elements).

**Common Inline Elements**:
- `<span>`: A generic container for inline text.
- `<a>`: Defines a hyperlink.
- `<strong>`: Indicates important text (usually rendered in bold).
- `<em>`: Emphasizes text (usually rendered in italics).
- `<img>`: Embeds an image.
- `<br>`: Inserts a line break.
- `<code>`: Represents a fragment of computer code.
- `<i>`: Displays text in italics (without semantic emphasis).
- `<b>`: Displays text in bold (without semantic importance).

**Usage Example**:
```html
<p>This is a <strong>bold</strong> word and this is <em>italic</em>.</p>
```

#### 3. **Mixed Usage**
You can mix block and inline elements to create complex layouts. For example, you can place inline elements within block elements to enhance text or add links.

**Example**:
```html
<section>
    <h2>My Favorite Books</h2>
    <p>I love reading <a href="#">fantasy</a> and <span>science fiction</span> books.</p>
</section>
```

### Symbols in HTML 5

| **Symbol**  | **Entity Name**       | **Numeric Code** | **Description**                  |
|-------------|-----------------------|------------------|----------------------------------|
| `&`         | `&amp;`               | `&#38;`          | Ampersand                        |
| `<`         | `&lt;`                | `&#60;`          | Less than                       |
| `>`         | `&gt;`                | `&#62;`          | Greater than                     |
| `"`         | `&quot;`              | `&#34;`          | Double quote                     |
| `'`         | `&apos;`              | `&#39;`          | Single quote                     |
| `©`         | `&copy;`              | `&#169;`         | Copyright symbol                 |
| `®`         | `&reg;`               | `&#174;`         | Registered trademark symbol      |
| `™`         | `&trade;`             | `&#8482;`        | Trademark symbol                 |
| `•`         | `&bull;`              | `&#8226;`        | Bullet point                     |
| `—`         | `&mdash;`             | `&#8212;`        | Em dash                          |
| `–`         | `&ndash;`             | `&#8211;`        | En dash                          |
| `°`         | `&deg;`               | `&#176;`         | Degree symbol                    |
| `€`         | `&euro;`              | `&#8364;`        | Euro sign                        |
| `£`         | `&pound;`             | `&#163;`         | British pound sign               |
| `¥`         | `&yen;`               | `&#165;`         | Japanese yen sign                |
| `¢`         | `&cent;`              | `&#162;`         | Cent sign                        |
| `¶`         | `&para;`              | `&#182;`         | Pilcrow (paragraph sign)         |
| `§`         | `&sect;`              | `&#167;`         | Section sign                     |
| `∞`         | `&infin;`             | `&#8734;`        | Infinity symbol                  |
| `≤`         | `&le;`                | `&#8804;`        | Less than or equal to           |
| `≥`         | `&ge;`                | `&#8805;`        | Greater than or equal to        |

### Layout Reflow/DOM Reflow

**DOM Reflow** (also known as layout reflow) is the process by which the browser recalculates the positions and sizes of elements in the Document Object Model (DOM) after changes have been made to the document's structure, style, or content. This is an essential aspect of rendering web pages, and understanding it can help developers optimize performance.

#### 1. **What Causes Reflow?**
Reflow can be triggered by various actions, including:

- **Adding or Removing Elements**: Inserting or deleting elements changes the overall layout.
- **Changing Element Attributes**: Modifying attributes that affect layout, such as `width`, `height`, `margin`, `padding`, and `border`.
- **Changing Styles**: Applying CSS styles that affect the size or position of elements, such as display properties or positioning.
- **Resizing the Browser Window**: Altering the viewport dimensions can affect the layout.
- **Modifying Text Content**: Changing the text inside elements can affect their size and therefore the layout.

#### 2. **How Reflow Works**
When reflow occurs, the browser follows these steps:

1. **Change Detection**: The browser identifies what has changed in the DOM.
2. **Recalculate Styles**: The browser recalculates styles for affected elements, applying any relevant CSS rules.
3. **Layout Calculation**: The browser determines the new positions and sizes of elements in the layout based on the updated styles.
4. **Rendering**: The browser repaints the affected elements, updating the display on the screen.

#### 3. **Performance Implications**
Reflow can be resource-intensive, especially if it affects many elements or if it occurs frequently. Here are some considerations:

- **Cost of Reflow**: Reflow is generally more expensive than repainting because it involves complex calculations. Frequent reflows can lead to performance issues, causing sluggishness in user interactions.
- **Batch DOM Changes**: To minimize reflows, batch DOM updates. Instead of making multiple individual changes, group them together so the browser only needs to reflow once.
- **Use CSS for Animations**: When animating elements, prefer CSS transitions and animations over JavaScript, as they can often optimize performance by minimizing reflows.

#### 4. **Avoiding Unnecessary Reflows**
To enhance performance and reduce the frequency of reflows:

- **Use Document Fragments**: When adding multiple elements, create them in a `DocumentFragment` and append them to the DOM in one operation.
- **Minimize Style Changes**: Change styles that require reflow only when necessary.
- **Use `requestAnimationFrame`**: For animations or updates, use `requestAnimationFrame` to synchronize changes with the browser's refresh rate, resulting in smoother animations and fewer reflows.

## L2.5 Styling (08:31)

CSS (Cascading Style Sheets) is a stylesheet language used to describe the presentation of a document written in HTML or XML. It allows you to control the layout, colors, fonts, spacing, and overall design of web pages.

### 1. **Selectors**
Selectors are patterns used to select the elements you want to style. Common types include:

- **Element Selector**: Targets HTML tags (e.g., `p` for paragraphs).
- **Class Selector**: Targets elements with a specific class (e.g., `.classname`).
- **ID Selector**: Targets a unique element with a specific ID (e.g., `#idname`).
- **Attribute Selector**: Targets elements based on attributes (e.g., `[type="text"]`).

### 2. **Properties and Values**
CSS properties define what aspect of the element you want to change. Each property is followed by a value, such as:

```css
color: blue;           /* Text color */
font-size: 16px;      /* Font size */
margin: 10px;         /* Space around an element */
padding: 5px;         /* Space inside an element */
background-color: #f0f0f0; /* Background color */
```

### 3. **Box Model**
The box model is a fundamental concept that describes how elements are structured in CSS:

- **Content**: The actual content of the box (text, images).
- **Padding**: Space between the content and the border.
- **Border**: A border around the padding (if any).
- **Margin**: Space outside the border that separates the element from others.

### 4. **Layout Techniques**
CSS provides several techniques for layout:

- **Flexbox**: A layout model that allows for flexible and responsive designs.
- **Grid**: A two-dimensional layout system for arranging elements in rows and columns.
- **Float**: An older method for layout, primarily used for text wrapping around images.

### 5. **Responsive Design**
To make web pages look good on all devices, CSS supports:

- **Media Queries**: Allows you to apply styles based on the device's characteristics (like width).
  
  ```css
  @media (max-width: 600px) {
      body {
          background-color: lightblue;
      }
  }
  ```

### 6. **Styling Text**
You can style text using properties like:

- `font-family`: Specifies the font.
- `font-weight`: Adjusts the boldness of the text.
- `line-height`: Sets the spacing between lines of text.

### 7. **Transitions and Animations**
CSS can create smooth transitions and animations:

- **Transitions**: Changes from one style to another over a specified duration.

  ```css
  button {
      transition: background-color 0.5s;
  }

  button:hover {
      background-color: blue;
  }
  ```

- **Animations**: More complex changes that can involve keyframes.

### 8. **Variables and Custom Properties**
CSS supports custom properties (also known as CSS variables), allowing for reuse of values:

```css
:root {
    --main-color: #3498db;
}

h1 {
    color: var(--main-color);
}
```


### CSS Specificity or Precedence

CSS precedence, also known as specificity, determines which styles are applied when there are conflicting rules. Understanding how CSS prioritizes different selectors is crucial for effective styling. Here’s a breakdown of the key concepts:

#### 1. **Specificity Hierarchy**
Specificity is calculated based on the types of selectors used. The more specific the selector, the higher its priority. Specificity is determined using a four-part value, often represented as (a, b, c, d):

- **a**: Inline styles (e.g., `style="..."` in an HTML element). This has the highest specificity.
- **b**: ID selectors (e.g., `#idname`). Each ID adds 1 to this value.
- **c**: Class selectors, attribute selectors, and pseudo-classes (e.g., `.classname`, `[type="text"]`, `:hover`). Each of these adds 1.
- **d**: Element selectors and pseudo-elements (e.g., `p`, `::before`). Each adds 1.

##### Example:
For the selectors:
- `h1` (0, 0, 0, 1)
- `.header` (0, 0, 1, 0)
- `#main` (0, 1, 0, 0)
- `style="color: red;"` (1, 0, 0, 0)

If all are applied to an element, the inline style will take precedence, followed by the ID, class, and then the element.

#### 2. **Cascading Order**
If selectors have the same specificity, the last one defined in the CSS file will take precedence due to the cascading nature of CSS. 

#### 3. **Importance of the `!important` Rule**
You can override specificity by using the `!important` declaration:

```css
p {
    color: blue !important;
}

#text {
    color: red;
}
```

In this case, the paragraph will always be blue, regardless of any other conflicting styles unless another `!important` rule is applied.

#### 4. **Inheritance**
Some properties inherit values from their parent elements (like `color`, `font-family`, etc.), while others do not (like `margin`, `padding`). If a child element doesn’t have a specific style, it will inherit from its parent.

#### 5. **Grouping Selectors**
You can group selectors to apply the same styles to multiple elements, but this doesn't increase specificity:

```css
h1, h2, h3 {
    color: green;
}
```

#### 6. **Common Mistakes**
- Overusing `!important`: It can make debugging difficult and lead to unintended results.
- Not understanding specificity can result in styles not being applied as expected.

## L2.6 Types of CSS Styling and Responsive websites (17:07)

### Style Specificity Over riding

1. Inline CSS
2. ID based CSS (#id)
3. Class based CSS (.class)

### Separation of Concerns

Separating content from style in web frontends is a fundamental principle in web design and development that enhances maintainability, accessibility, and performance. This process involves using different technologies to handle the content (HTML), presentation (CSS), and behavior (JavaScript). Here’s a detailed overview of how to achieve this separation:

#### 1. **Use of HTML for Content**
HTML (HyperText Markup Language) is used to structure the content of a web page. It defines elements such as headings, paragraphs, links, images, and forms without concerning itself with how these elements will be displayed.

- **Semantic HTML**: Use HTML elements that describe their meaning (e.g., `<header>`, `<footer>`, `<article>`, `<nav>`) to improve accessibility and SEO.

##### Example:
```html
<article>
    <h1>Title of the Article</h1>
    <p>This is the content of the article.</p>
</article>
```

#### 2. **Use of CSS for Styling**
CSS (Cascading Style Sheets) is used to control the presentation of the HTML content. It defines how elements are displayed, including layout, colors, fonts, spacing, and responsiveness.

- **External Stylesheets**: Keep CSS in separate files rather than inline styles within HTML. This allows for easier maintenance and reusability.

##### Example:
```css
article {
    font-family: Arial, sans-serif;
    color: #333;
    margin: 20px;
}

h1 {
    color: #0056b3;
}
```

- **Linking CSS**: Use a `<link>` tag in the HTML to connect the CSS file.

```html
<head>
    <link rel="stylesheet" href="styles.css">
</head>
```

#### 3. **Use of JavaScript for Behavior**
JavaScript handles dynamic behavior and interactivity on the web page. It can manipulate the DOM (Document Object Model), allowing you to change content or styles based on user actions.

- **External Scripts**: Similar to CSS, keep JavaScript in separate files for better organization and maintenance.

##### Example:
```javascript
document.getElementById("myButton").addEventListener("click", function() {
    alert("Button clicked!");
});
```

- **Linking JavaScript**: Include the script in the HTML using the `<script>` tag.

```html
<body>
    <button id="myButton">Click Me</button>
    <script src="script.js"></script>
</body>
```

#### 4. **Benefits of Separation**
- **Maintainability**: Easier to update styles or scripts without altering the HTML structure.
- **Reusability**: CSS and JavaScript can be reused across multiple pages.
- **Performance**: Browsers cache external CSS and JavaScript files, improving load times.
- **Accessibility**: Improved semantic structure enhances accessibility for screen readers and other assistive technologies.

#### 5. **Using Frameworks and Tools**
Utilizing frameworks (like Bootstrap for CSS or React for JavaScript) can help maintain this separation while providing pre-built components and utilities. Additionally, preprocessors like SASS or LESS for CSS can help manage styles more effectively.
### Responsive Web Pages

A **responsive webpage** is designed to provide an optimal viewing experience across a wide range of devices, from desktops to smartphones. This approach ensures that users can easily read and navigate the site without needing to zoom or scroll horizontally. Here are the key principles and best practices for creating responsive web pages:

#### Key Principles of Responsive Web Design

1. **Fluid Grids**: Use relative units like percentages instead of fixed units like pixels for layout elements. This allows elements to resize proportionally.

2. **Flexible Images**: Ensure images scale with the layout by using CSS properties such as `max-width: 100%;` so that images do not overflow their containing elements.

3. **Media Queries**: Utilize CSS media queries to apply different styles based on the device's characteristics, such as width, height, and orientation.

4. **Viewport Meta Tag**: Include the viewport meta tag in the HTML to control the layout on mobile browsers. This is essential for making web pages responsive.

   ```html
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   ```

#### Best Practices for Responsive Web Design

1. **Mobile-First Approach**: Start designing for the smallest screens first, then progressively enhance the design for larger screens. This helps prioritize essential content and ensures a better user experience on mobile devices.

2. **Grid Systems**: Use a responsive grid system (like Bootstrap or CSS Grid) to manage layout easily. This helps align content neatly across different screen sizes.

3. **Breakpoints**: Define breakpoints based on the content, not device sizes. Common breakpoints include:
   - 320px (mobile devices)
   - 768px (tablets)
   - 1024px (desktops)

   Adjust the layout and styles as needed at these breakpoints.

4. **Responsive Typography**: Use relative units (like `em` or `rem`) for font sizes to ensure text scales well across devices. Consider using responsive units like `vw` (viewport width) for headings.

5. **Touch-Friendly Elements**: Make sure buttons and links are large enough for easy tapping on touch devices. The recommended size is at least 44x44 pixels.

6. **Testing Across Devices**: Test your design on various devices and screen sizes. Use browser developer tools to simulate different viewports.

7. **Optimize Media**: Serve appropriately sized images for different devices. Use formats like WebP for better compression and faster loading times. Consider using the `<picture>` element for responsive images.

   ```html
   <picture>
       <source srcset="image-small.jpg" media="(max-width: 600px)">
       <source srcset="image-large.jpg" media="(min-width: 601px)">
       <img src="image-large.jpg" alt="Description">
   </picture>
   ```

8. **Minimize the Use of Fixed Widths**: Avoid using fixed widths for elements, as they can break layouts on smaller screens. Use percentages, `auto`, or `flex` properties instead.

9. **Progressive Enhancement**: Ensure that the core content and functionality are accessible without advanced features. Enhance with CSS and JavaScript for devices that support them.

10. **Use Frameworks**: Leverage responsive frameworks (like Bootstrap or Foundation) that provide pre-designed components and a grid system, making it easier to create responsive layouts.

### CSS shorthand properties

CSS shorthand properties allow you to set multiple related CSS properties in a single declaration, making your stylesheets more concise and easier to read.

### 1. **Margin and Padding**
You can set the `margin` and `padding` for all four sides (top, right, bottom, left) in one declaration.

```css
/* All sides */
margin: 10px; /* 10px for top, right, bottom, left */

/* Vertical | Horizontal */
margin: 10px 20px; /* 10px top/bottom | 20px left/right */

/* Top | Horizontal | Bottom */
margin: 10px 20px 15px; /* 10px top | 20px left/right | 15px bottom */

/* Top | Right | Bottom | Left */
margin: 10px 15px 20px 25px; /* top | right | bottom | left */
```

### 2. **Borders**
You can define the `border` width, style, and color in a single line.

```css
border: 2px solid red; /* 2px width | solid style | red color */
```

You can also use shorthand for individual sides:

```css
border-top: 2px solid red; /* Top border only */
```

### 3. **Background**
The `background` shorthand can include several properties like color, image, position, size, repeat, and attachment.

```css
background: #ff0000 url('image.jpg') no-repeat center center; /* Color | Image | Repeat | Position */
```

### 4. **Font**
You can set multiple font properties in one shorthand declaration.

```css
font: italic bold 16px/1.5 "Arial", sans-serif; /* Style | Weight | Size/Line-height | Font-family */
```

### 5. **List Style**
The `list-style` property combines `list-style-type`, `list-style-position`, and `list-style-image`.

```css
list-style: disc inside url('marker.png'); /* Type | Position | Image */
```

### 6. **Transition**
You can define multiple properties for transitions in one line.

```css
transition: all 0.3s ease-in-out; /* Property | Duration | Timing function */
```

### 7. **Flexbox**
You can set multiple flex properties in one shorthand declaration.

```css
flex: 1 0 100px; /* flex-grow | flex-shrink | flex-basis */
```

### 8. **Grid**
Shorthand properties for CSS Grid include `grid` and `grid-area`.

```css
grid: 1fr 2fr / 100px 200px; /* Rows / Columns */
```

#### Benefits of Using Shorthand
- **Conciseness**: Reduces the amount of code, making stylesheets smaller and easier to manage.
- **Readability**: Groups related properties together, improving the readability of the code.
- **Performance**: Less CSS can lead to slightly faster loading times since there’s less data to download.

`border`, `background`, `font`, `margin`, `inset`


### CSS Positioning

CSS positioning allows you to control the layout and placement of elements on a web page. There are several positioning methods in CSS, each serving different purposes. Here’s a breakdown of the main types of positioning, along with examples for each.

#### 1. **Static Positioning**
Static positioning is the default positioning method. Elements are placed in the normal document flow, and their position is determined by their order in the HTML.

##### Example:
```html
<div class="box">Static Box 1</div>
<div class="box">Static Box 2</div>
```

```css
.box {
    background: lightblue;
    margin: 10px;
    padding: 20px;
}
```

#### 2. **Relative Positioning**
Relative positioning moves an element relative to its original position in the document flow. The space for the element remains, so it does not affect the layout of surrounding elements.

##### Example:
```html
<div class="relative-box">I am a relative box</div>
```

```css
.relative-box {
    position: relative;
    top: 20px;   /* Moves down from its original position */
    left: 10px;  /* Moves right from its original position */
    background: lightgreen;
    padding: 20px;
}
```

#### 3. **Absolute Positioning**
Absolute positioning removes an element from the normal document flow and positions it relative to the nearest positioned ancestor (an ancestor with a position other than `static`). If there is no such ancestor, it positions relative to the initial containing block (usually the viewport).

##### Example:
```html
<div class="container">
    <div class="absolute-box">I am an absolute box</div>
</div>
```

```css
.container {
    position: relative; /* Positioned ancestor */
    height: 200px;
    background: lightgray;
}

.absolute-box {
    position: absolute;
    top: 10px;   /* 10px from the top of the container */
    left: 10px;  /* 10px from the left of the container */
    background: lightcoral;
    padding: 20px;
}
```

#### 4. **Fixed Positioning**
Fixed positioning removes an element from the document flow and positions it relative to the viewport. The element remains fixed in place when the page is scrolled.

##### Example:
```html
<div class="fixed-box">I am a fixed box</div>
```

```css
.fixed-box {
    position: fixed;
    bottom: 20px; /* 20px from the bottom of the viewport */
    right: 20px;  /* 20px from the right of the viewport */
    background: lightyellow;
    padding: 20px;
}
```

#### 5. **Sticky Positioning**
Sticky positioning is a hybrid of relative and fixed positioning. An element with `position: sticky` behaves like a relative element until it reaches a defined scroll position, after which it behaves like a fixed element.

##### Example:
```html
<div class="sticky-box">I am a sticky box</div>
```

```css
.sticky-box {
    position: sticky;
    top: 0; /* Sticks to the top of the viewport */
    background: lightpink;
    padding: 20px;
}
```

#### Summary of Positioning Types
- **Static**: Default positioning, in normal document flow.
- **Relative**: Positioned relative to its original location.
- **Absolute**: Positioned relative to the nearest positioned ancestor, removed from document flow.
- **Fixed**: Positioned relative to the viewport, remains in place on scroll.
- **Sticky**: Acts like relative until a certain scroll position, then acts like fixed.

### CSS Selectors and Combinators

CSS selectors and combinators are fundamental concepts that allow you to target and style specific HTML elements in a web document. Understanding how to use them effectively is essential for creating well-structured and visually appealing styles. Here’s an overview of the different types of CSS selectors and combinators:

### CSS Selectors

1. **Universal Selector (`*`)**
   - Selects all elements on the page.
   - Example:
     ```css
     * {
         margin: 0;
         padding: 0;
     }
     ```

2. **Type Selector (Element Selector)**
   - Selects all instances of a specific HTML element.
   - Example:
     ```css
     p {
         color: blue;
     }
     ```

3. **Class Selector (`.`)**
   - Selects all elements with a specified class attribute.
   - Example:
     ```css
     .highlight {
         background-color: yellow;
     }
     ```

4. **ID Selector (`#`)**
   - Selects a single element with a specified ID attribute (IDs should be unique within a document).
   - Example:
     ```css
     #header {
         font-size: 24px;
     }
     ```

5. **Attribute Selector**
   - Selects elements based on the presence or value of a specific attribute.
   - Examples:
     ```css
     /* Selects all input elements with a type of text */
     input[type="text"] {
         border: 1px solid gray;
     }

     /* Selects all anchor tags with a title attribute */
     a[title] {
         color: green;
     }
     ```

6. **Pseudo-class Selector**
   - Selects elements based on their state or position.
   - Examples:
     ```css
     /* Selects all links that have been visited */
     a:visited {
         color: purple;
     }

     /* Selects the first child of any element */
     p:first-child {
         font-weight: bold;
     }
     ```

7. **Pseudo-element Selector**
   - Selects a part of an element, like the first line or first letter.
   - Examples:
     ```css
     /* Selects the first letter of a paragraph */
     p::first-letter {
         font-size: 2em;
     }

     /* Selects the first line of a paragraph */
     p::first-line {
         font-style: italic;
     }
     ```

### CSS Combinators

Combinators define the relationship between two or more selectors. There are four main types:

1. **Descendant Combinator (space)**
   - Selects elements that are descendants (children, grandchildren, etc.) of a specified element.
   - Example:
     ```css
     .container p {
         color: red; /* Selects all <p> elements within elements with class 'container' */
     }
     ```

2. **Child Combinator (`>`)**
   - Selects only the direct children of a specified element.
   - Example:
     ```css
     ul > li {
         list-style-type: none; /* Selects only direct <li> children of <ul> */
     }
     ```

3. **Adjacent Sibling Combinator (`+`)**
   - Selects an element that is immediately next to another specified element.
   - Example:
     ```css
     h1 + p {
         margin-top: 0; /* Selects the first <p> immediately following an <h1> */
     }
     ```

4. **General Sibling Combinator (`~`)**
   - Selects all siblings that follow a specified element.
   - Example:
     ```css
     h1 ~ p {
         color: gray; /* Selects all <p> elements that follow an <h1> */
     }
     ```

### CSS Child manipulations

CSS child manipulation refers to styling and selecting elements based on their relationship to their parent elements in the DOM (Document Object Model). This allows you to apply styles specifically to child elements of a parent

#### 1. **Direct Child Selector (`>`)**
The direct child selector (`>`) selects only the elements that are direct children of a specified parent. This is useful when you want to apply styles to only immediate child elements.

##### Example:
```html
<div class="parent">
    <div class="child">Child 1</div>
    <div class="child">Child 2</div>
    <div class="nested">
        <div class="child">Nested Child</div>
    </div>
</div>
```

```css
.parent > .child {
    background-color: lightblue;
    padding: 10px;
}
```
In this example, only "Child 1" and "Child 2" will have a light blue background, while "Nested Child" will not be styled because it’s not a direct child of `.parent`.

#### 2. **General Sibling Selector (`~`)**
The general sibling selector (`~`) selects elements that are siblings (share the same parent) and come after the specified element.

##### Example:
```html
<div class="parent">
    <div class="sibling">Sibling 1</div>
    <div class="sibling">Sibling 2</div>
    <div class="sibling">Sibling 3</div>
</div>
```

```css
.sibling:nth-child(2) ~ .sibling {
    background-color: lightgreen;
}
```
In this case, "Sibling 3" will have a light green background because it follows "Sibling 2".

#### 3. **Child Combinator (`:nth-child()` and `:nth-of-type()`)**
These pseudo-classes allow you to select child elements based on their order or type.

- **`:nth-child(n)`**: Selects the nth child of a parent, regardless of type.
- **`:nth-of-type(n)`**: Selects the nth child of a specific type (e.g., div, p) among siblings.

##### Example:
```html
<div class="list">
    <p>Paragraph 1</p>
    <p>Paragraph 2</p>
    <p>Paragraph 3</p>
    <div>Div 1</div>
</div>
```

```css
.list p:nth-child(2) {
    color: red; /* Styles the second paragraph */
}

.list p:nth-of-type(2) {
    font-weight: bold; /* Styles the second paragraph of type p */
}
```

#### 4. **First and Last Child Selectors**
These selectors allow you to specifically target the first or last child element within a parent.

##### Example:
```html
<ul class="menu">
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>
```

```css
.menu li:first-child {
    font-weight: bold; /* Styles the first item */
}

.menu li:last-child {
    color: blue; /* Styles the last item */
}
```

#### 5. **Nested Child Selectors**
You can apply styles to deeper levels of nesting using combinations of child selectors.

##### Example:
```html
<div class="outer">
    <div class="inner">
        <p>Inner Paragraph</p>
    </div>
</div>
```

```css
.outer .inner p {
    color: purple; /* Styles the paragraph inside .inner */
}
```


### Pseudo Elements

| **Pseudo-Element** | **Description**                                           | **Example**                              |
|---------------------|-----------------------------------------------------------|------------------------------------------|
| `::after`           | Inserts content after the element's content.             | `p::after { content: " [more]"; }`     |
| `::before`          | Inserts content before the element's content.            | `p::before { content: "Note: "; }`     |
| `::first-line`      | Styles the first line of a block of text.                | `p::first-line { font-weight: bold; }` |
| `::first-letter`    | Styles the first letter of a block of text.              | `p::first-letter { font-size: 2em; }`  |
| `::selection`       | Styles the portion of an element that is selected by the user. | `::selection { background: yellow; }`  |
| `::placeholder`     | Styles the placeholder text in input fields.             | `input::placeholder { color: gray; }`  |
| `::marker`          | Styles the marker box of a list item.                    | `li::marker { color: red; }`           |
| `::backdrop`        | Styles the backdrop of an element when it is displayed in a modal context (e.g., `<dialog>`). | `dialog::backdrop { background: rgba(0,0,0,0.5); }` |
| `::spelling-error`  | Styles text that has a spelling error.                   | `::spelling-error { text-decoration: underline; }` |
| `::grammar-error`   | Styles text that has a grammar error.                    | `::grammar-error { background: yellow; }` |

### Notes:
- **Syntax**: Pseudo-elements are generally denoted with `::`, but for backward compatibility, some pseudo-elements (like `::before` and `::after`) may still be seen with a single `:` in older styles.
- **Usage Context**: These pseudo-elements are often used to enhance the design and user experience of web pages, allowing for targeted styling without adding extra HTML elements.
## BootStrap

### Bootstrap Grid Layout
#### Overview of Bootstrap Grid System

1. **12-Column Layout**: The Bootstrap grid system is based on a 12-column layout. This means that any row can be divided into up to 12 equal-width columns.

2. **Flexbox**: Bootstrap uses Flexbox to ensure that columns can grow and shrink as needed, allowing for more flexible layouts.

3. **Responsive Design**: Bootstrap's grid system is responsive, meaning it automatically adjusts to different screen sizes. It uses a series of media queries to apply styles at various breakpoints.

#### Column Classes

Bootstrap provides a set of classes that you can use to create columns in your layout. Here’s a breakdown:

- **Basic Column Classes**: You can use `.col` to create equal-width columns.

  ```html
  <div class="row">
      <div class="col">Column 1</div>
      <div class="col">Column 2</div>
      <div class="col">Column 3</div>
  </div>
  ```

- **Column Widths**: You can specify how many columns an element should span using `.col-{breakpoint}-{number}` classes. Here are some examples:

  - **Extra Small (xs)**: For screens less than 576px.
  - **Small (sm)**: For screens ≥576px.
  - **Medium (md)**: For screens ≥768px.
  - **Large (lg)**: For screens ≥992px.
  - **Extra Large (xl)**: For screens ≥1200px.
  - **Extra Extra Large (xxl)**: For screens ≥1400px (available in Bootstrap 5).

  ```html
  <div class="row">
      <div class="col-6">Column 1 (50%)</div>
      <div class="col-6">Column 2 (50%)</div>
  </div>
  ```

  ```html
  <div class="row">
      <div class="col-sm-4">Column 1 (33.33%)</div>
      <div class="col-sm-8">Column 2 (66.67%)</div>
  </div>
  ```

#### Column Offsetting

You can also offset columns to create space between them. For example, to offset a column by a certain number of columns:

```html
<div class="row">
    <div class="col-md-4">Column 1</div>
    <div class="col-md-4 offset-md-4">Column 2 (offset 4)</div>
</div>
```

##### Nesting Columns

You can nest columns within a column by creating a new `.row` inside an existing column.

```html
<div class="row">
    <div class="col-md-6">
        <div class="row">
            <div class="col-6">Nested Column 1</div>
            <div class="col-6">Nested Column 2</div>
        </div>
    </div>
    <div class="col-md-6">Column 2</div>
</div>
```

#### Responsive Utilities

Bootstrap provides utility classes to show or hide columns at specific breakpoints. For instance, you can use `d-none d-md-block` to hide a column on small devices but show it on medium devices and up.

#### Example Layout

Here’s a complete example of a Bootstrap grid layout:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/css/bootstrap.min.css">
    <title>Bootstrap Columns Example</title>
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-md-4">Column 1</div>
            <div class="col-md-4">Column 2</div>
            <div class="col-md-4">Column 3</div>
        </div>
        <div class="row">
            <div class="col-md-6">Column 4</div>
            <div class="col-md-6">Column 5</div>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```
### Bootstrap Best Practices

Using Bootstrap effectively can greatly enhance your web development process, leading to responsive and visually appealing websites. Here are some best practices to consider when working with Bootstrap:

#### 1. **Use the Grid System Wisely**
- **Understand the 12-Column Grid**: Familiarize yourself with how the grid system works to create layouts that are responsive and well-structured.
- **Avoid Fixed Widths**: Use percentage-based or grid classes to ensure elements adapt to different screen sizes.
- **Nest Columns**: Use nested rows and columns to create complex layouts, but be cautious not to over-nest, as it can lead to increased complexity.

#### 2. **Utilize Bootstrap Components**
- **Leverage Built-in Components**: Use Bootstrap's pre-designed components (e.g., navbars, cards, modals) to save time and maintain consistency across your application.
- **Customize Components**: Customize components using Bootstrap’s utility classes or your own styles to match your branding while maintaining responsiveness.

#### 3. **Mobile-First Approach**
- **Start with Mobile Styles**: Design with smaller screens in mind first and then use media queries or Bootstrap classes to enhance for larger devices. This approach aligns with Bootstrap's responsive design philosophy.

#### 4. **Minimize Custom CSS**
- **Use Bootstrap Classes**: Take advantage of Bootstrap's utility classes to avoid writing excessive custom CSS. This makes your code cleaner and easier to maintain.
- **Override Carefully**: If you need custom styles, be specific in your CSS selectors to avoid unintended overrides of Bootstrap styles.

#### 5. **Optimize Performance**
- **Include Only What You Need**: Use a custom build of Bootstrap or selectively include only the components you need to reduce file size.
- **Minimize HTTP Requests**: Combine CSS and JavaScript files where possible to reduce the number of HTTP requests.

#### 6. **Responsive Utilities**
- **Use Responsive Classes**: Use Bootstrap's responsive utility classes (like `.d-none`, `.d-md-block`, etc.) to show or hide elements at different breakpoints, allowing for a cleaner and more adaptable layout.
- **Image Responsiveness**: Use the `.img-fluid` class to make images responsive and avoid layout shifts.

#### 7. **Accessibility Considerations**
- **Semantic HTML**: Use appropriate HTML elements (like `<nav>`, `<header>`, and `<footer>`) to improve accessibility and SEO.
- **Aria Attributes**: Where necessary, add ARIA attributes to enhance accessibility for users with disabilities.

#### 8. **Consistent Design**
- **Use Bootstrap’s Theme**: Stick to Bootstrap's default styles and components for a consistent look and feel.
- **Custom Themes**: If creating a custom theme, ensure consistency in spacing, font sizes, and colors to create a cohesive design.

#### 9. **Testing Across Devices**
- **Cross-Browser Testing**: Test your website on various browsers and devices to ensure consistent performance and appearance.
- **Responsive Design Testing**: Use browser developer tools to test responsiveness at different screen sizes.

#### 10. **Keep Documentation Handy**
- **Bootstrap Documentation**: Refer to the official Bootstrap documentation for guidelines, examples, and best practices. It’s a valuable resource for troubleshooting and discovering new features.

#### 11. **Stay Updated**
- **Version Updates**: Keep your Bootstrap version updated to benefit from new features, performance improvements, and security patches.
