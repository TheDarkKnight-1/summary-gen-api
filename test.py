from summary_gen import generate_summary

text="Hello everyone welcome back to this wonderful journey of computer organisation and architecture. In this session we will be focusing on memory. So let's get to learning. Wikipedia state memory is the faculty of brain by which data or information is encoded. Store and retrieve when needed. Similarly in case of computer memory which was initially termed as law plays a similar role. Everything beat an image and audio file to text file or instructions for a key press or a mouse click if that is stored in the computer memory is actually encoded as b. Basically each memory cell can have either 0 or 1. And all the at comprised of millions of b and process by the processor the brain of the computer. So we might think that having a single large memory unit is the solution to the situation. But i'm afraid it's not. With the increasing size of the memory the time to access them gets increased and time is there a sincere liquid put it to you this way. We know the processor is very fast i am in today we have ghz processor even in our smartphone. Suppose we have 2 ghz processor. This means the frequency is 2 ghz. Time is one upon frequency. That is. 1 by 2 into 10 to the power 9. How did i get this 10 to the power 9. Chat shelvi v no 1 kilo unit equals to 1000 unit has 10 cube unit. Therefore one mega unit is 1000 kilo unit and the 10 to the power 6 units and finally 1 giga unit is 1000 units and the 10 to the power 9 unit. Not coming back to our initial illustration 1 upon 2 into 10 to the power 9 s equals to 1 by 2 into 10 to the power minus 9 sec. And 10 to the power minus 9 seconds is 1 nanosecond. Therefore in half ns our processor can perform a single task. To conclude the cpu is fast. Not only fat. Real fat. And keeping up with this kind of speed is tough. Because if our memory device is way slower than the cpu then the cpu will remain idle for the most of the time and we won't have an efficient machine also not only the speed the size and the cost are considered to when it comes to memory that's why we have various memory devices associated to our computer. Computer designers term the memory to perform immediate stars as primary memory. In the memory which is used as a more permanent storage is known as secondary mein. When we play an audio file our system manager that is the operating system manages the space within the primary memory. To perform the instruction which is understanding the mouse click opening up the default application for playing the file after bringing it from the secondary storage into the primary memory. Us because we need the execution of the instructions to be as quick as possible the sales in the primary memory can be accessed in any order and that's why the name random access memory or ram. To be precise it actually dynamic ram because in each memory chip there is a transistor with which a capacitor is associated the transistors can retain the binary bit as long as the associated capacitors has charge. Superior degree charging is needed for value retention. And that's why it's called dynamic. But it still slow for the modern day processor so we opt for another first memory storage that cache cache is made up of static ram which doesn't have any capacitors but they are very costly in comparison to the main or primary memory. However cashew happens to be the fastest memory storage among all other. Anyway all these be that cache or main memory are volatile. That means they can only retain the data in them until the power is off. Therefore to store the data more permanently we opt for the next type of memory storage. The secondary member. Secondary memory is a slower than the main memory. Yah dekhen retain data permanent. That is the data inside them are still there even if the power is off. Their larger in terms of capacity also they are cheaper than the main memory. Will definitely get into the detail study of various types of secondary memories in our due course. But for the time being i'd like to take an example of one of the most popular secondary storage devices that is the hard disk drive to explain one of the reasons why these a slower compared to the main memory. Hard disk drive the access is my random. Now why so because using this read write hate we can randomly get to any of these tracks but from their getting to the particular block with the data is stored requires sequential movement. The time to access any data in the hard describe becomes longer naturally. Now let me show you the big picture. We have the processor and it has got its registers but these are not capable of storing large amount of data. To be really honest the can be released for the single instruction so we opt for main memory. Main memory is also for the processor so we store the frequently accessed in a smaller it faster than main memory speed memory storage the cache. It's like keeping our phones in our pocket instead of the backpack that we are caring because we tend to use the phone very frequently. The main memory and the cache communicate using data word or block. In the ways the communication takes place is known as cache memory mapping. Worry not we will learn every type of these in details later. So having this organisation does speed things up or not. But none of these retain data permanently. So we need a permanent non-volatile storage this secondary memory. Using the virtual memory mapping technique the operating system let the main memory and the auxiliary secondary storage communicate with one another using pages. What this to happen the operating system must be capable of performing paging or demand paging. Fun fact. The processor is aware of the presence of the registers the caches even the main memory but it has got no clue about the existence of the secondary memory. There the operating system comes at rescue and manages all the things. So to conclude having a single large memory is not really a solution instead we use different types of storage unit in an organised fashion. So that was all for this situation in the next one will get into the details of this memory storage is and learn about the memory hierarchy. Hope to see you in the next one thank you all for watching. "

print("Summary: \n"+ generate_summary(text))