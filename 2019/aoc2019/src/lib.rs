use std::error::Error;
use std::io::BufRead;

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

pub fn day2_part1(input: Box<dyn BufRead>) -> Result<Vec<i32>, Box<dyn Error>> {
    let mut memory: Vec<i32> = input
        .lines()
        .next()
        .unwrap()
        .unwrap()
        .split(',')
        .map(|ch|
            ch.parse().unwrap()
        ).collect();

    memory[1] = 12;
    memory[2] = 2;

    day2::run_intcode_program(&mut memory);

    Ok(memory)
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
    pub fn run_intcode_program(memory: &mut Vec<i32>) {
        let mut instr_ptr = 0;
        let mut instr = memory[instr_ptr];
        while instr != 99 {
            if instr == 1 {
                // addition
                let arg1_loc = memory[instr_ptr + 1] as usize;
                let arg2_loc = memory[instr_ptr + 2] as usize;
                let result_loc = memory[instr_ptr + 3] as usize;
                memory[result_loc] = memory[arg1_loc] + memory[arg2_loc];
            } else if instr == 2 {
                // multiplication
                let arg1_loc = memory[instr_ptr + 1] as usize;
                let arg2_loc = memory[instr_ptr + 2] as usize;
                let result_loc = memory[instr_ptr + 3] as usize;
                memory[result_loc] = memory[arg1_loc] * memory[arg2_loc];
            }
            instr_ptr += 4;
            instr = memory[instr_ptr];
        }
    }
}