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
