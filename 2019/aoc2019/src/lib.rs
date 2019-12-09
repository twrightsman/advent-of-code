use std::error::Error;
use std::io::BufRead;

use itertools::Itertools;

pub fn day1_part1(input: Box<dyn BufRead>) -> Result<i32, Box<dyn Error>> {
    let result: i32 = input.lines()
        .map(|line| {
            day1::mass_to_fuel(line.unwrap().parse::<i32>().unwrap())
        })
        .sum();
    
    Ok(result)
}

pub fn day1_part2(input: Box<dyn BufRead>) -> Result<i32, Box<dyn Error>> {
    let result: i32 = input.lines()
        .map(|line| {
            day1::mass_to_total_fuel(line.unwrap().parse::<i32>().unwrap())
        })
        .sum();
    
    Ok(result)
}

pub fn day2_part1(input: Box<dyn BufRead>) -> Result<i32, Box<dyn Error>> {
    let mut memory = day2::parse_memory(input);

    memory[1] = 12;
    memory[2] = 2;

    day2::run_intcode_program(&mut memory);

    Ok(memory[0])
}

pub fn day2_part2(input: Box<dyn BufRead>) -> Result<i32, &'static str> {
    let memory = day2::parse_memory(input);

    // test combinations of nouns and verbs
    for (noun, verb) in (0..100).cartesian_product(0..100) {
        let mut memory = memory.clone();
        memory[1] = noun;
        memory[2] = verb;
        day2::run_intcode_program(&mut memory);
        if memory[0] == 19690720 {
            return Ok((100 * noun) + verb);
        }
    }

    Err("Couldn't find the magic noun/verb combination")
}

pub mod day1 {
    pub fn mass_to_fuel(mass: i32) -> i32 {
        (((mass as f32) / 3.0).floor() as i32) - 2
    }

    pub fn mass_to_total_fuel(mass: i32) -> i32 {
        let mut total_fuel = mass_to_fuel(mass);
        let mut extra_fuel = mass_to_fuel(total_fuel);

        while extra_fuel > 0 {
            total_fuel += extra_fuel;
            extra_fuel = mass_to_fuel(extra_fuel);
        }

        total_fuel
    }
}

pub mod day2 {
    use std::io::BufRead;

    pub fn parse_memory(input: Box<dyn BufRead>) -> Vec<i32> {
        input
        .lines()
        .next()
        .unwrap()
        .unwrap()
        .split(',')
        .map(|ch|
            ch.parse().unwrap()
        ).collect()
    }

    pub fn run_intcode_program(memory: &mut Vec<i32>) {
        let mut instr_ptr = 0;
        let mut instr = memory[instr_ptr];
        while instr != 99 {
            if instr == 1 {
                // addition
                let arg1_addr = memory[instr_ptr + 1] as usize;
                let arg2_addr = memory[instr_ptr + 2] as usize;
                let result_addr = memory[instr_ptr + 3] as usize;
                memory[result_addr] = memory[arg1_addr] + memory[arg2_addr];
            } else if instr == 2 {
                // multiplication
                let arg1_addr = memory[instr_ptr + 1] as usize;
                let arg2_addr = memory[instr_ptr + 2] as usize;
                let result_addr = memory[instr_ptr + 3] as usize;
                memory[result_addr] = memory[arg1_addr] * memory[arg2_addr];
            }
            instr_ptr += 4;
            instr = memory[instr_ptr];
        }
    }
}