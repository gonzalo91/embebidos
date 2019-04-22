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


       $sql = 'SELECT *, IF (totalDeDias > 0, ROUND(totalPorDia / totalDeDias), 0) total FROM ( SELECT DAYOFWEEK(started_at) AS dia, COUNT(1) totalPorDia FROM parks_in AS perDay GROUP BY DAYOFWEEK(started_at) ) totalEntradas INNER JOIN ( SELECT COUNT(1) totalDeDias, t.dia FROM ( SELECT DAYOFWEEK(started_at) AS dia FROM parks_in GROUP BY DAYOFWEEK(started_at), DAY(started_at), MONTH(started_at) ) AS t GROUP BY t.dia ) AS totalDias ON totalEntradas.dia = totalDias.dia';

        $firstChart = DB::select($sql);

        dd($firstChart);
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

//        foreach($firstChart as $data)
//            $dataFirstChart .= $data->cuenta.',';
////        dd($dataFirstChart);
        return view('index', compact('dataFirstChart'));
    }
}
