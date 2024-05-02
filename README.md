<div align="center">
  <h1>MIPS R4000 Simulator for an 8-Stage Pipeline</h1>
  <h2>By Sofiia Druchyna</h2>
</div>

### Overview

This project is a part of CMPS 6661: Advanced Computer Architecture at Tulane University. I build a MIPS R4000 simulator (from the MIPS64 family) that 
for an eight-stage pipeline. The processor uses deeper pipeline than the simple 5-stage design. This deeper pipeline allows it to achieve higher clock rates by decomposing the five-stage integer pipeline into 8 stages. 
Since the cache access stages are usually on the critical path, the extra pipeline stages come from decomposing the memory access stages to achieve more balanced pipeline stages.

### Pipeline Description
The defined pipeline has eight stages. Although the instruction and data memory occupy multiple cycles, they are fully pipelined, so that a new instruction can start on every clock. The function of each stage is given as follows: (NOTE: The stages described below are different from those of MIPS 4000.)

- **IF** - First half of instruction fetch. PC (Program Counter) selection actually happens here, together with initiation of instruction cache access.
- **IS** - Second half of instruction fetch, complete instruction cache access. Note that in this project we assume instruction accesses always hit the instruction cache.
- **ID** - Instruction decode, hazard checking.
- **RF** - Register fetch.
- **EX** - Execution, which includes effective address calculation, ALU operation, and branch-target computation and condition evaluation.
- **DF** - Data fetch, first half of data cache access.
- **DS** - Second half of data fetch, completion of data cache access. Note that the data access always hit the data cache.
- **WB** - Write back for loads and register-register operations.

### Hazard Handling

**Load hazard stalls:**
In addition to substantially increasing the amount of forwarding required, this longer-latency pipeline increases both the load and branch delays. This is encountered when RAW register dependence results from a memory load instruction. In this case, the new register value is not known until after the DS stage since it must be loaded from memory. 
If an instruction is immediately followed the load and needs the value in the EX stage, two stall cycles must be inserted.

**Branch hazard stalls:**
Since branches are resolved during EX, the basic branch delay is 4 cycles. In this project assume that there is no delayed branch. We use a predicted-not-taken strategy for reducing the branch delay. Therefore, for untaken branches, there will be no delay. However, if the outcome is taken, the instruction in the IF, IS, ID and RF stages must be cancelled (four bubbles) and the target instruction will be fetched at the next cycle. 
For unconditional jumps, four stall cycles are always created.

### Forwarding
There are several stages in the pipeline where forwarding is possible:

- EX/DF => RF/EX
- DF/DS => EX/DF
- DF/DS => RF/EX
- DS/WB => EX/DF
- DS/WB => RF/EX

### Output
MIPS R4000 simulator ran for 147 cycles on the given input (fibonacci code). At each cycle, the simulator displayed the current PC, pipeline status, totall stalls (load/branch), forwarding at each stage, pipeline registers, integer registers (R0-R31), data in memory, and total number of forwarding operations.

### Usage
The code is written in a single file named "Simulator". The "Disassembler" directory must be downloaded along with the main one, so the simulator can decode the binary code before interpreting and executing the instructions. No additional dependencies are required to launch the simulator.
