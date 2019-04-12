<?php

use Faker\Generator as Faker;

$factory->define(App\Park::class, function (Faker $faker) {
    return [
        'name' => 'loza',
        'url'  => 'https://zalollauri.embebidos.app.heroku.com',
        'full_spaces' => 7
    ];
});
