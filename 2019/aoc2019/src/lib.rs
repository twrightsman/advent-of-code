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

pub fn day3_part1(input: Box<dyn BufRead>) -> Result<u32, &'static str> {
    let wires: Vec<String> = input.lines().map(|l| {l.unwrap()}).collect();

    Ok(day3::closest_intersection(&wires[0], &wires[1]))
}

pub fn day3_part2(input: Box<dyn BufRead>) -> Result<u32, &'static str> {
    let wires: Vec<String> = input.lines().map(|l| {l.unwrap()}).collect();

    Ok(day3::fewest_steps(&wires[0], &wires[1]))
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

pub mod day3 {
    use std::collections::HashMap;
    use std::convert::TryFrom;

    #[derive(Debug, PartialEq)]
    pub enum WireInstr {
        Up(u32),
        Down(u32),
        Right(u32),
        Left(u32)
    }

    #[derive(Debug, PartialEq, Eq, Hash, Clone, Copy)]
    pub struct Point {
        pub x: i32,
        pub y: i32
    }

    impl WireInstr {
        pub fn new(instr_str: &str) -> Result<Self, String> {
            let mut instr_str_chars = instr_str.chars();
            let dir_str = instr_str_chars.next().unwrap();
            let dist: u32 = instr_str_chars.collect::<String>().parse().unwrap();

            if dir_str == 'U' {
                return Ok(Self::Up(dist))
            } else if dir_str == 'D' {
                return Ok(Self::Down(dist))
            } else if dir_str == 'R' {
                return Ok(Self::Right(dist))
            } else if dir_str == 'L' {
                return Ok(Self::Left(dist))
            } else {
                return Err(format!("Invalid direction: {}", dir_str))
            }
        }
    }

    pub fn parse_wire_string(wire: &str) -> Result<Vec<WireInstr>, &'static str> {
        let result = wire.split(',')
            .map(|instr_str| {
                WireInstr::new(instr_str).unwrap()
            })
            .collect();

        Ok(result)
    }

    pub fn wire_points(wire: Vec<WireInstr>) -> Vec<Point> {
        let mut points: Vec<Point> = vec![];
        let mut grid_pos = Point{x: 0, y: 0};

        for instr in wire.iter() {
            match instr {
                WireInstr::Up(dist) => {
                    let new_y = grid_pos.y + i32::try_from(*dist).unwrap();
                    for y in (grid_pos.y + 1)..=new_y {
                        points.push(Point{x: grid_pos.x, y: y})
                    }
                    grid_pos.y = new_y;
                },
                WireInstr::Down(dist) => {
                    let new_y = grid_pos.y - i32::try_from(*dist).unwrap();
                    for y in (new_y..grid_pos.y).rev() {
                        points.push(Point{x: grid_pos.x, y: y})
                    }
                    grid_pos.y = new_y;
                },
                WireInstr::Right(dist) => {
                    let new_x = grid_pos.x + i32::try_from(*dist).unwrap();
                    for x in (grid_pos.x + 1)..=new_x {
                        points.push(Point{x: x, y: grid_pos.y})
                    }
                    grid_pos.x = new_x;
                },
                WireInstr::Left(dist) => {
                    let new_x = grid_pos.x - i32::try_from(*dist).unwrap();
                    for x in (new_x..grid_pos.x).rev() {
                        points.push(Point{x: x, y: grid_pos.y})
                    }
                    grid_pos.x = new_x;
                }
            }
        }

        points
    }

    pub fn wire_intersects(wire1: &Vec<Point>, wire2: &Vec<Point>) -> Vec<Point> {
        let mut points = HashMap::new();

        for (p1, p2) in wire1.iter().zip(wire2.iter()) {
            points.entry(p1).or_insert([0, 0])[0] += 1;
            points.entry(p2).or_insert([0, 0])[1] += 1;
        }

        let mut intersections: Vec<Point> = vec![];
        for (&key, &_value) in points.iter().filter(|(&_k, &v)| {(v[0] > 0) && (v[1] > 0)}) {
            intersections.push(*key);
        }

        intersections
    }

    pub fn manhattan_distance(p1: Point, p2: Point) -> u32 {
        u32::try_from((p1.x - p2.x).abs() + (p1.y - p2.y).abs()).unwrap()
    }

    pub fn steps_to_point(p: Point, wire: &Vec<Point>) -> Result<u32, &'static str> {
        // find first occurance of p in wire
        let mut i = 1; // start at one to include origin
        for point in wire.iter() {
            if *point == p {
                return Ok(i)
            }
            i += 1;
        }

        Err("Couldn't find point in wire")
    }

    pub fn fewest_steps(wire1_str: &str, wire2_str: &str) -> u32 {
        let wire1_points = wire_points(parse_wire_string(wire1_str).unwrap());
        let wire2_points = wire_points(parse_wire_string(wire2_str).unwrap());
        let mut intersects = wire_intersects(
            &wire1_points,
            &wire2_points
        );

        intersects.sort_by(|a, b| {
            (steps_to_point(*a, &wire1_points).unwrap() + steps_to_point(*a, &wire2_points).unwrap()).partial_cmp(&(steps_to_point(*b, &wire1_points).unwrap() + steps_to_point(*b, &wire2_points).unwrap())).unwrap()});

        steps_to_point(intersects[0], &wire1_points).unwrap() + steps_to_point(intersects[0], &wire2_points).unwrap()
    }

    pub fn closest_intersection(wire1_str: &str, wire2_str: &str) -> u32 {
        let ctrl_port = Point{x: 0, y: 0};
        let mut intersects = wire_intersects(
            &wire_points(parse_wire_string(wire1_str).unwrap()),
            &wire_points(parse_wire_string(wire2_str).unwrap())
        );
        intersects.sort_by(|a, b| {manhattan_distance(ctrl_port, *a).partial_cmp(&manhattan_distance(ctrl_port, *b)).unwrap()});

        manhattan_distance(ctrl_port, intersects[0])
    }
}