use std::io::{self, BufRead};

use aoc2019;

fn main() {
    let stdin = io::stdin();
    let handle = stdin.lock();
    let result: f32 = handle.lines()
        .map(|line| {
            aoc2019::mass_to_fuel(line.unwrap().parse::<f32>().unwrap())
        })
        .sum();
    
    println!("{}", result)
}
