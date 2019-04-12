<?php

use App\Park_In;
use App\Park;
use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     *
     * @return void
     */
    public function run()
    {
        // $this->call(UsersTableSeeder::class);

        factory(App\Park::class, 1)->create();
        factory(App\Park_In::class, 200)->create();

    }
}
