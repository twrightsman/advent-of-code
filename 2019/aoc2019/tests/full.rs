use std::fs::File;
use std::io;

use aoc2019;

#[test]
fn day1_part1_full() {
    let file = File::open("inputs/day1.txt");
    let reader = Box::new(io::BufReader::new(file.unwrap()));

    assert_eq!(aoc2019::day1_part1(reader).unwrap(), 3474920);
}

#[test]
fn day1_part2_full() {
    let file = File::open("inputs/day1.txt");
    let reader = Box::new(io::BufReader::new(file.unwrap()));

    assert_eq!(aoc2019::day1_part2(reader).unwrap(), 5209504);
}

#[test]
fn day2_part1_full() {
    let file = File::open("inputs/day2.txt");
    let reader = Box::new(io::BufReader::new(file.unwrap()));

    assert_eq!(aoc2019::day2_part1(reader).unwrap(), 2890696);
}

#[test]
fn day2_part2_full() {
    let file = File::open("inputs/day2.txt");
    let reader = Box::new(io::BufReader::new(file.unwrap()));

    assert_eq!(aoc2019::day2_part2(reader).unwrap(), 8226);
}

#[test]
fn day3_part1_full() {
    let file = File::open("inputs/day3.txt");
    let reader = Box::new(io::BufReader::new(file.unwrap()));

    assert_eq!(aoc2019::day3_part1(reader).unwrap(), 1017);
}