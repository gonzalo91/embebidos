<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateParksInTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('parks_in', function (Blueprint $table) {
            $table->bigIncrements('id');
            $table->integer('park_id')->unsigned();
            $table->foreign('park_id')->references('id')->on('parks');
            $table->integer('sensor_id')->nullable();
            $table->dateTime('started_at');
            $table->dateTime('finished_at')->nullable();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('parks_in');
    }
}
