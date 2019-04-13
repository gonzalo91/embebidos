<?php

use Faker\Generator as Faker;
use Illuminate\Support\Facades\DB;

$factory->define(App\Park_In::class, function (Faker $faker) {
    $dateInitial = $faker->dateTimeBetween($startDate = '-1 MONTH', $endDate = 'now', $timezone='UTC');

    return [
        'park_id' => 1,
        'sensor_id' => $faker->numberBetween(1,7),
        'started_at' => $dateInitial,
        'finished_at' => $faker->dateTimeInInterval($startDate=$dateInitial, $interval = '+ 4 hour'),
    ];
});
