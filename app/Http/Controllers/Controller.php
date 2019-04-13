<?php

namespace App\Http\Controllers;

use Illuminate\Foundation\Bus\DispatchesJobs;
use Illuminate\Routing\Controller as BaseController;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use App\Park_In;
use Illuminate\Support\Facades\DB;

class Controller extends BaseController
{
    use AuthorizesRequests, DispatchesJobs, ValidatesRequests;



    public function index(){
        $firstChart;

        $sql = 'SELECT cast( sum(cuenta)/4 as UNSIGNED) cuenta FROM (SELECT count(DAYOFWEEK(cast(started_at as DATE))) cuenta, (DAYOFWEEK(cast(started_at as DATE))-1) as day FROM `parks_in` WHERE 1 GROUP BY DAYOFWEEK(cast(started_at as DATE)), cast(started_at as DATE)) as t GROUP BY day
';

        $firstChart = DB::select($sql);
        $dataFirstChart = '';

//        dd(collect($firstChart)->keyBy('cuenta'));
//        $countByDay = Park_In::select(DB::raw('count(1) cuenta'), DB::raw('cast(started_at as DATE) as started_at'))
//                ->groupBy(DB::raw( 'cast(started_at as DATE)'))
//                ->get();
//
//        $groupByDayOfWeek = Park_In::select(DB::raw('count(1) suma'), DB::raw('(DAYOFWEEK(started_at) -1) day'))
//                                ->groupBy(DB::raw('DAYOFWEEK(started_at) -1'))
//                                ->get();
//
//        dd('Cuenta',$countByDay, 'groupByDay', $groupByDayOfWeek);
//
//        foreach ($groupByDayOfWeek as $item) {
//            $arre[] = $countByDay->filter(function($object, $key) use ($item){
//
//                return $object->started_at->dayOfWeek == $item->day;
//            })->sum('cuenta') / $item->suma;
//        }
//    $dataFirstChart = collect($firstChart)->keyBy('cuenta')->keys()->implode(',');

        foreach($firstChart as $data)
            $dataFirstChart .= $data->cuenta.',';
//        dd($dataFirstChart);
        return view('index', compact('dataFirstChart'));
    }
}
