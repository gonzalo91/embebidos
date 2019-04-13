<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Park_In extends Model
{
    protected $table = 'parks_in';

    public $timestamps = false;

    protected $dates = [
        'started_at'
    ];
}
